# app.py
import base64
import streamlit as st
from datetime import datetime
from data import DESPACHO_DATA, SUGESTOES_PLANO, ESTOQUE_DATA, LIBERADO_DATA, PLANO_DESPACHO_DATA
from logic import generate_response
from ui_components import (
    plano_despacho_list, kpi_card, progress_card, sugestao_list, estoque_list, liberado_list, _image_to_base64, inject_global_css, assistant_header
)
import os, time

PAGE_TITLE = "Bino - Agente de Despacho Logístico"
PAGE_SUBTITLE = "Agente para otimização do despacho - Usiminas"

def init_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = [{
            "role": "assistant",
            "content": ("Olá! Eu sou o Bino, seu assistente de planejamento logístico. "
                        "Como posso ajudar com o plano de despacho hoje?"),
            "timestamp": datetime.now().strftime("%H:%M")
        }]
    if "focus_input" not in st.session_state:
        st.session_state.focus_input = False
    if "input_key" not in st.session_state:
        st.session_state.input_key = 0
    # Adicionar estado para controle da expansão do plano
    if "plano_expanded" not in st.session_state:
        st.session_state.plano_expanded = False

def header():
    st.set_page_config(page_title=PAGE_TITLE, page_icon="🚚", layout="wide")
    st.markdown(
        f"""
        <div style="padding:1rem; border-left: 4px solid #16A34A; 
                    background: white; border-radius: .5rem; margin-bottom: .75rem;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <div>
                    <h2 style="margin:0">{PAGE_TITLE}</h2>
                    <p style="margin:.25rem 0; color:#4B5563">{PAGE_SUBTITLE}</p>
                </div>
                <div style="text-align:right">
                    <div style="font-size:.9rem; color:#6B7280">Data: {datetime.now().strftime('%d/%m/%Y')}</div>
                    <div style="font-size:.9rem; color:#16A34A; font-weight:600">Sistema Online</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# app.py - Modifique a função left_panel()

def left_panel():
    st.markdown("#### Despacho Mensal")
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        kpi_card(
            title="Diário Online",
            value=f"{DESPACHO_DATA['diaAnterior']} ton",
            color="#3B82F6",
            icon="📅"
        )
    with c2:
        kpi_card(
            title="Acumul. Mensal",
            value=f"{DESPACHO_DATA['acumulMensal']:,} ton".replace(",", "."),
            color="#22C55E",
            icon="📈"
        )
    with c3:
        kpi_card(
            title="Plano Acumul.",
            value=f"{DESPACHO_DATA['planoAcumul']:,} ton".replace(",", "."),
            color="#A855F7",
            icon="📊"
        )
    with c4:
        progress_card(
            title="Desvio",
            value=f"{'+' if DESPACHO_DATA['desvio'] > 0 else ''}{DESPACHO_DATA['desvio']} ton",
            pct=(DESPACHO_DATA["acumulMensal"]/DESPACHO_DATA["planoAcumul"])*100,
            positive=DESPACHO_DATA["desvio"] >= 0
        )
    
    # Barra de progresso com cor verde
    st.markdown("""
        <style>
            .stProgress > div > div > div > div {
                background-color: #16A34A;
            }
        </style>
    """, unsafe_allow_html=True)
    st.progress(DESPACHO_DATA["capacidadeUtilizada"] / 100.0, text=f"Capacidade de Despacho Diária Utilizada: {DESPACHO_DATA['capacidadeUtilizada']}%")

    st.markdown("#### Sugestões do Bino")
    
    # MODIFICAÇÃO AQUI: Adicionar a aba "Plano de Despacho"
    tab1, tab2, tab3, tab4 = st.tabs(["Plano de Despacho", "Crítico", "Estoque", "OVs Liberadas"])
    
    with tab1:
        # Inicializar estado da expansão se não existir
        if "plano_expanded" not in st.session_state:
            st.session_state.plano_expanded = False
            
        # Componente do plano de despacho
        plano_despacho_list(PLANO_DESPACHO_DATA, st.session_state.plano_expanded)
    
    with tab2:
        sugestao_list(SUGESTOES_PLANO)
    
    #with tab3:
        # Reexibe os KPIs principais de "Despacho" para ficar próximo à UI original
        #st.caption("Indicadores de Despacho")
        #c1, c2, c3 = st.columns(3)
        #with c1:
        #    st.metric("Dia Anterior", f"{DESPACHO_DATA['diaAnterior']} ton")
        #with c2:
        #    st.metric("Acumul. Mensal", f"{DESPACHO_DATA['acumulMensal']:,} ton".replace(",", "."))
        #with c3:
        #    st.metric("Plano Acumul.", f"{DESPACHO_DATA['planoAcumul']:,} ton".replace(",", "."))
    
    with tab3:
        estoque_list(ESTOQUE_DATA)
    
    with tab4:
        liberado_list(LIBERADO_DATA)

def chat_panel():
    inject_global_css()
    
    st.markdown("#### Assistente Bino")
    
    # Container principal do chat
    #st.markdown('<div class="bino-chat-main">', unsafe_allow_html=True)
    
    # Header
    avatar_file = os.path.join("assets", "Bino-Linkedin.jpg")
    
    # Renderizar histórico de mensagens
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            # Mensagem do usuário (alinhada à direita)
            st.markdown(
                f"""
                <div class="bino-message user">
                    <div class="bino-message-bubble">
                        {msg["content"]}
                        <div class="user-message-timestamp" color='white' style="text-align: right;">{msg["timestamp"]}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            # Mensagem do assistente (alinhada à esquerda)
            avatar_img = ""
            if os.path.exists(avatar_file):
                with open(avatar_file, "rb") as f:
                    avatar_base64 = base64.b64encode(f.read()).decode()
                    avatar_img = f'<img class="bino-avatar" src="data:image/jpeg;base64,{avatar_base64}" />'
            else:
                avatar_img = '<div class="bino-avatar"></div>'
            
            st.markdown(
                f"""
                <div class="bino-message assistant">
                    {avatar_img}
                    <div class="bino-message-bubble">
                        {msg["content"]}
                        <div class="bino-message-timestamp">{msg["timestamp"]}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
    
    # ÁREA PARA O INDICADOR DE DIGITAÇÃO
    typing_placeholder = st.empty()
    
    st.markdown('</div>', unsafe_allow_html=True)  # Fecha área de mensagens
    
    # Área de input - MAIOR E MAIS EVIDENTE
    st.markdown('<div class="bino-input-container">', unsafe_allow_html=True)
    
    # Input do chat - usando st.chat_input nativo com estilo melhorado
    if "pending_prompt" not in st.session_state:
        st.session_state.pending_prompt = None
    
    # JavaScript para focar e rolar para o input APÓS CADA RESPOSTA
    if st.session_state.get("focus_input", False):
        st.markdown("""
            <script>
                function focusAndScrollToInput() {
                    const inputContainer = document.querySelector('.bino-input-container');
                    const input = document.querySelector('.stChatInput textarea');
                    
                    if (inputContainer && input) {
                        // Rola suavemente para o container de input
                        inputContainer.scrollIntoView({ 
                            behavior: 'smooth', 
                            block: 'center'
                        });
                        
                        // Foca no campo de texto
                        input.focus();
                        
                        console.log('Foco e scroll aplicados após resposta do Bino');
                    } else {
                        // Tenta novamente se não encontrar os elementos
                        setTimeout(focusAndScrollToInput, 200);
                    }
                }
                
                // Executa imediatamente
                focusAndScrollToInput();
            </script>
        """, unsafe_allow_html=True)
        # Reseta o estado após aplicar o foco
        st.session_state.focus_input = False
    
    # Usar st.chat_input que é mais adequado para chat - COM MAIS LINHAS
    user_input = st.chat_input(
        "Digite sua pergunta para o Bino...", 
        key=f"chat_input_{st.session_state.input_key}"
    )
    
    # Quick Actions - AGORA POSICIONADO LOGO ABAIXO DO CAMPO DE INPUT
    st.markdown('<div class="bino-quick-actions">', unsafe_allow_html=True)
    st.markdown('<div class="quick-actions-title">Ações rápidas:</div>', unsafe_allow_html=True)
    
    # Criar colunas para os botões - MAIS DISCRETOS
    cols = st.columns(4)
    quick_actions = [
        ("📊 Desempenho", "Qual o desempenho dos despachos?"),
        ("🛣️ Rotas", "Sugerir rotas para hoje"), 
        ("📦 Estoque", "Verificar estoque disponível"),
        ("🚚 Capacidade", "Verificar capacidade disponível")
    ]
    
    for i, (label, prompt) in enumerate(quick_actions):
        with cols[i]:
            if st.button(label, key=f"quick_{i}", use_container_width=True):
                st.session_state.pending_prompt = prompt
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)  # Fecha quick actions
    
    # Processar input pendente das quick actions
    final_prompt = user_input or st.session_state.pending_prompt
    
    if final_prompt:
        # Limpar prompt pendente
        if st.session_state.pending_prompt:
            st.session_state.pending_prompt = None
        
        # Adicionar mensagem do usuário
        user_timestamp = datetime.now().strftime("%H:%M")
        st.session_state.messages.append({
            "role": "user",
            "content": final_prompt,
            "timestamp": user_timestamp
        })
        
        # Mostrar indicador de digitação NO LUGAR CORRETO (logo após as mensagens)
        with typing_placeholder:
            avatar_img = ""
            if os.path.exists(avatar_file):
                with open(avatar_file, "rb") as f:
                    avatar_base64 = base64.b64encode(f.read()).decode()
                    avatar_img = f'<img class="bino-avatar" src="data:image/jpeg;base64,{avatar_base64}" />'
            else:
                avatar_img = '<div class="bino-avatar"></div>'
            
            st.markdown(
                f"""
                <div class="bino-message assistant">
                    {avatar_img}
                    <div class="bino-message-bubble">
                        <div class="bino-typing">
                            Digitando
                            <span class="bino-dot"></span>
                            <span class="bino-dot"></span>
                            <span class="bino-dot"></span>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        # Simular processamento
        time.sleep(1.5)
        typing_placeholder.empty()
        
        # Gerar resposta
        response = generate_response(final_prompt)
        response_timestamp = datetime.now().strftime("%H:%M")
        
        # Adicionar resposta ao histórico
        st.session_state.messages.append({
            "role": "assistant", 
            "content": response,
            "timestamp": response_timestamp
        })
        
        # MARCA PARA FOCAR E ROLAR APÓS A RESPOSTA DO ASSISTENTE
        st.session_state.focus_input = True
        st.session_state.input_key += 1  # Força re-render do input
        
        # Rerun para atualizar a interface
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)  # Fecha input container

def main():
    init_session_state()
    header()
    
    # Layout responsivo
    left_col, right_col = st.columns([1.2, 1.8], gap="large")
    
    with left_col:
        left_panel()
    
    with right_col:
        chat_panel()

    # Adicione um pouco de espaço no final
    st.markdown("<div style='height: 20px'></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()