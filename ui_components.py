# ui_components.py
import streamlit as st
from pathlib import Path
import base64

def kpi_card(title: str, value: str, color: str = "#16A34A", icon: str = "✅"):
    st.markdown(
        f"""
        <div style="
            border:1px solid #E5E7EB; border-radius:.5rem; padding:.75rem;
            background: #F8FAFC;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:.25rem;">
                <span style="font-size:.85rem; color:#6B7280; font-weight:600">{title}</span>
                <span style="font-size:1rem">{icon}</span>
            </div>
            <div style="font-size:1.4rem; font-weight:800; color:#111827">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

def progress_card(title: str, value: str, pct: float, positive: bool = True):
    bg = "#ECFDF5" if positive else "#FEF2F2"
    border = "#A7F3D0" if positive else "#FECACA"
    color = "#059669" if positive else "#DC2626"
    st.markdown(
        f"""
        <div style="border:1px solid {border}; border-radius:.5rem; padding:.75rem; background:{bg}">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:.25rem;">
                <span style="font-size:.85rem; color:#6B7280; font-weight:600">{title}</span>
                <span style="font-size:1rem">⚠️</span>
            </div>
            <div style="font-size:1.4rem; font-weight:800; color:{color}">{value}</div>
            <div style="font-size:.75rem; color:#6B7280"> {pct:.1f}% da meta</div>
        </div>
        """,
        unsafe_allow_html=True
    )

def badge(text: str, style: str):
    colors = {
        "OV Crítica": ("#FEE2E2", "#B91C1C"),
        "Média": ("#FEF3C7", "#B45309"),
        "Baixa": ("#F3F4F6", "#374151")
    }
    bg, fg = colors.get(style, ("#F3F4F6", "#374151"))
    return f'<span style="font-size:.75rem; padding:.15rem .5rem; border-radius:999px; background:{bg}; color:{fg}; font-weight:600">{style}</span>'

def chip(text: str, color="#16A34A", bg="#ECFDF5"):
    return f'<span style="font-size:.75rem; padding:.15rem .5rem; border-radius:999px; background:{bg}; color:{color}; font-weight:600">{text}</span>'

# ui_components.py - Atualize a função sugestao_list

def sugestao_list(items):
    st.caption(f"💡 Sugestões otimizadas para hoje — Total: {sum(int(i['quantidade'].split()[0]) for i in items)} ton em {len(items)} despachos")
    for s in items:
        st.markdown(
            f"""
            <div style="border:1px solid #E5E7EB; border-radius:.5rem; padding:.6rem; margin-bottom:.5rem; background:white">
                <div style="display:flex; justify-content:space-between; align-items:flex-start;">
                    <div style="font-weight:700; color:#111827">{s['id']}</div>
                    {badge(s['prioridade'], s['prioridade'])}
                </div>
                <div style="font-size:.9rem; color:#374151; font-weight:600">{s['cliente']}</div>
                <div style="font-size:.9rem; color:#4B5563; margin:.2rem 0 .4rem 0">{s['produto']} - {s['quantidade']}</div>
                <div style="display:flex; justify-content:space-between; font-size:.8rem;">
                    <span style="color:#6B7280">📍 {s['destino']}</span>
                    <div style="display:flex; gap:.5rem">
                        {chip(s['usina'], color="#DC2626", bg="#FEE2E2")}
                        {chip(s['modal'], color="#2563EB", bg="#EFF6FF")}
                        {chip(s['caminhao'])}
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

def estoque_list(items):
    st.caption("📦 Visão geral do estoque (atualizado em tempo real)")
    for it in items:
        pct = (it["disponivel"]/it["estoque"]) if it["estoque"] else 0
        with st.container(border=True):
            st.markdown(f"**{it['produto']}**")
            c1, c2, c3 = st.columns(3)
            with c1: st.metric("Estoque Total", f"{it['estoque']} {it['unidade']}")
            with c2: st.metric("Reservado", f"{it['reservado']} {it['unidade']}")
            with c3: st.metric("Disponível", f"{it['disponivel']} {it['unidade']}")
            # Barra de progresso verde para estoque
            st.markdown("""
                <style>
                    .stProgress > div > div > div > div {
                        background-color: #16A34A;
                    }
                </style>
            """, unsafe_allow_html=True)
            st.progress(pct, text=f"Disponibilidade: {pct*100:.1f}%")

def liberado_list(items):
    st.caption(f"✅ Pedidos liberados para despacho — {len(items)} pedidos aguardando programação")
    for it in items:
        with st.container(border=True):
            c1, c2 = st.columns([2,1])
            with c1:
                st.markdown(f"**{it['id']}**")
                st.markdown(f"{it['cliente']}  \n{it['produto']} — {it['quantidade']}")
                st.caption(f"Liberado em: {it['dataLiberacao']}")
            with c2:
                st.markdown(
                    "<div style='text-align:right; margin-top:.2rem;'>"
                    "<span style='background:#ECFDF5; color:#16A34A; padding:.25rem .6rem; border-radius:999px; font-weight:700; font-size:.8rem'>Liberado</span>"
                    "</div>",
                    unsafe_allow_html=True
                )


def _image_to_base64(path: str) -> str:
    """Converte imagem para base64 para exibição em HTML"""
    try:
        from pathlib import Path
        import base64
        
        p = Path(path)
        if not p.exists():
            return ""
        with open(p, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    except Exception:
        return ""


def inject_global_css():
    st.markdown("""
    <style>
    /* Tipografia moderna */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
    html, body, [class*="css"] {
      font-family: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI',
                   Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', Arial, sans-serif !important;
    }

    /* Container principal do chat */
    .bino-chat-main {
        border: 1px solid #E5E7EB;
        border-radius: 16px;
        background: white;
        box-shadow: 0 4px 20px rgba(17, 24, 39, .08);
        overflow: hidden;
        margin-bottom: 1rem;
        height: 500px;
        overflow-y: auto;
        padding: 20px;
    }

    /* Header do chat */
    .bino-chat-header {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 16px 20px;
        background: linear-gradient(90deg, #F0FDF4, #FFFFFF);
        border-bottom: 1px solid #E5E7EB;
    }

    /* Estilos das mensagens */
    .bino-message {
        display: flex;
        gap: 12px;
        align-items: flex-start;
        margin-bottom: 20px;
    }

    .bino-message.user {
        justify-content: flex-end;
    }

    .bino-message.user .bino-message-bubble {
        background: #16A34A;
        color: white;
        border-radius: 18px 18px 4px 18px;
        box-shadow: 0 2px 8px rgba(22, 163, 74, 0.2);
    }

    .bino-message.assistant .bino-message-bubble {
        background: white;
        color: #111827;
        border: 1px solid #E5E7EB;
        border-radius: 18px 18px 18px 4px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    }

    .bino-message-bubble {
        padding: 14px 18px;
        max-width: 75%;
        line-height: 1.5;
        font-size: 0.95rem;
    }

    .bino-message-timestamp {
        font-size: 0.75rem;
        color: #6B7280;
        margin-top: 6px;
    }
                
    .user-message-timestamp {
        font-size: 0.75rem;
        color: rgba(255, 255, 255, 0.8);
        margin-top: 6px;
    }

    .bino-avatar {
        width: 38px;
        height: 38px;
        border-radius: 50%;
        border: 2px solid #16A34A;
        object-fit: cover;
        flex-shrink: 0;
    }

    /* Área de input - MAIOR E MAIS REFINADA */
    .bino-input-container {
        padding: 20px;
        background: white;
        border-top: 1px solid #E5E7EB;
        border-radius: 0 0 16px 16px;
        box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.04);
    }

    /* Quick actions - MAIS DISCRETOS E ORGANIZADOS */
    .bino-quick-actions {
        padding: 16px 0 0 0;
        background: white;
    }

    .quick-actions-title {
        font-size: 0.85rem;
        color: #6B7280;
        margin-bottom: 10px;
        font-weight: 600;
    }

    .bino-quick-actions .stButton > button {
        border: 1px solid #E5E7EB !important;
        background: #F8FAFC !important;
        color: #4B5563 !important;
        font-size: 0.8rem !important;
        padding: 6px 12px !important;
        border-radius: 12px !important;
        transition: all 0.2s ease !important;
        margin: 2px !important;
        font-weight: 500;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    }

    .bino-quick-actions .stButton > button:hover {
        border-color: #16A34A !important;
        color: #065F46 !important;
        background: #F0FDF4 !important;
        transform: translateY(-1px);
        box-shadow: 0 2px 4px rgba(22, 163, 74, 0.1);
    }

    /* Campo de input do chat MAIOR - 3 LINHAS */
    .stChatInput > div > div {
        border: 2px solid #E5E7EB !important;
        border-radius: 12px !important;
        background: #F8FAFC !important;
        transition: all 0.3s ease !important;
        min-height: 80px !important; /* Aumentado para 3 linhas */
    }

    .stChatInput textarea {
        min-height: 60px !important; /* Altura aumentada */
        line-height: 1.5 !important;
        padding: 12px 16px !important;
        font-size: 0.95rem !important;
    }

    .stChatInput > div > div:focus-within {
        border-color: #16A34A !important;
        background: white !important;
        box-shadow: 0 0 0 3px rgba(22, 163, 74, 0.1) !important;
    }

    /* Botão de enviar melhorado */
    .stChatInputContainer button {
        background: #16A34A !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        margin: 8px !important;
    }

    .stChatInputContainer button:hover {
        background: #15803D !important;
        transform: translateY(-1px);
    }

    /* Animação de digitação */
    .bino-typing {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        color: #065F46;
        font-style: italic;
        font-size: 0.9rem;
    }

    .bino-dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: #10B981;
        opacity: 0.4;
        animation: bino-blink 1.4s infinite;
    }

    .bino-dot:nth-child(2) { animation-delay: 0.2s; }
    .bino-dot:nth-child(3) { animation-delay: 0.4s; }

    @keyframes bino-blink {
        0%, 100% { opacity: 0.4; }
        50% { opacity: 1; }
    }

    /* Scrollbar personalizada */
    .bino-chat-main::-webkit-scrollbar {
        width: 6px;
    }

    .bino-chat-main::-webkit-scrollbar-track {
        background: #F1F5F9;
    }

    .bino-chat-main::-webkit-scrollbar-thumb {
        background: #CBD5E1;
        border-radius: 3px;
    }

    /* Barras de progresso verdes */
    .stProgress > div > div > div > div {
        background-color: #16A34A !important;
    }

    /* Responsividade */
    @media (max-width: 768px) {
        .bino-message-bubble {
            max-width: 85%;
        }
        
        .bino-chat-main {
            height: 400px;
        }
        
        .stChatInput > div > div {
            min-height: 70px !important;
        }
        
        .stChatInput textarea {
            min-height: 50px !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Funções auxiliares para avatar/header (mantidas para compatibilidade)
def assistant_header(title: str, subtitle: str, avatar_path: str):
    """Cabeçalho do chat com avatar."""
    left, right = st.columns([0.12, 0.88])
    with left:
        p = Path(avatar_path)
        if p.exists():
            st.image(str(p), width=48, caption=None)
        else:
            st.markdown(
                "<div style='width:48px;height:48px;border-radius:50%;border:2px solid #16A34A;background:#E5E7EB'></div>",
                unsafe_allow_html=True
            )
    with right:
        st.markdown(f"<div style='font-weight:700; font-size:1.1rem;'>{title}</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='color:#16A34A; font-size:0.9rem;'>{subtitle}</div>", unsafe_allow_html=True)

# ui_components.py - Adicione esta função ao arquivo existente

# ui_components.py - Adicione esta função

# ui_components.py - Atualize a função plano_despacho_list

# ui_components.py - Atualize a função plano_despacho_list para fonte menor na visão expandida

# ui_components.py - Atualize a função plano_despacho_list para formatar números com 2 casas decimais

def plano_despacho_list(plano_data, expanded=False):
    """Componente para exibir o plano de despacho com opção de expandir/recolher"""
    
    st.caption("📋 Plano de Despacho - Visão Consolidada")
    
    # Botão para expandir/recolher
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("📊 Ver Planilha Completa" if not expanded else "📋 Ver Resumo", 
                    use_container_width=True, key="toggle_planilha"):
            st.session_state.plano_expanded = not expanded
            st.rerun()
    
    # Função auxiliar para formatar números com 2 casas decimais
    def format_number(value):
        """Formata número para 2 casas decimais, tratando valores zero e negativos"""
        if value == 0:
            return "0.00"
        elif isinstance(value, (int, float)):
            return f"{value:.2f}"
        else:
            return str(value)
    
    if not expanded:
        # VISÃO RESUMIDA
        st.markdown("#### 📈 Resumo do Despacho")
        
        # Cards principais com cores baseadas nos valores
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            delta_color = "normal" if plano_data['total_geral']['hoje_liberado'] > plano_data['total_geral']['dia_anterior_real'] else "inverse"
            st.metric(
                "Hoje - Liberado", 
                f"{format_number(plano_data['total_geral']['hoje_liberado'])} kt",
                delta=f"{format_number(plano_data['total_geral']['dia_anterior_real'])} kt ontem",
                delta_color=delta_color
            )
        with c2:
            delta_color = "normal" if plano_data['total_geral']['acumulado_delta'] >= 0 else "inverse"
            st.metric(
                "Acumulado Real", 
                f"{format_number(plano_data['total_geral']['acumulado_real'])} kt",
                delta=f"{format_number(plano_data['total_geral']['acumulado_delta'])} kt vs plano",
                delta_color=delta_color
            )
        with c3:
            st.metric(
                "Previsão Manhã", 
                f"{format_number(plano_data['clientes_diretos']['total']['previsao_manha'])} kt"
            )
        with c4:
            delta_color = "normal" if plano_data['clientes_diretos']['total']['liberado'] > plano_data['clientes_diretos']['total']['previsao_manha'] else "inverse"
            eficiencia = (plano_data['clientes_diretos']['total']['liberado']/plano_data['clientes_diretos']['total']['previsao_manha'])*100 if plano_data['clientes_diretos']['total']['previsao_manha'] > 0 else 0
            st.metric(
                "Eficiência", 
                f"{eficiencia:.1f}%",
                delta_color=delta_color
            )
        
        # Clientes Diretos - Resumo
        st.markdown("#### 🏭 Clientes Diretos")
        
        # Total Usinas vs CDs
        total_usinas = sum(usina['liberado'] for usina in plano_data['clientes_diretos']['usinas'])
        total_cds = sum(cd['liberado'] for cd in plano_data['clientes_diretos']['cds'])
        
        usina_cols = st.columns(2)
        with usina_cols[0]:
            st.metric("Total Usinas", f"{format_number(total_usinas)} kt")
        with usina_cols[1]:
            st.metric("Total CDs", f"{format_number(total_cds)} kt")
        
        # Principais usinas
        st.markdown("**Principais Usinas**")
        usinas_data = plano_data['clientes_diretos']['usinas']
        usinas_cols = st.columns(len(usinas_data))
        for i, usina in enumerate(usinas_data):
            with usinas_cols[i]:
                delta_color = "normal" if usina['liberado'] > usina['previsao_manha'] else "inverse"
                st.metric(
                    usina['nome'],
                    f"{format_number(usina['liberado'])} kt",
                    delta=f"{format_number(usina['previsao_manha'])} kt previsto",
                    delta_color=delta_color
                )
        
        # Principais CDs
        st.markdown("**Principais CDs**")
        cds_data = [cd for cd in plano_data['clientes_diretos']['cds'] if cd['liberado'] > 0][:4]
        if cds_data:
            cds_cols = st.columns(len(cds_data))
            for i, cd in enumerate(cds_data):
                with cds_cols[i]:
                    delta_color = "normal" if cd['liberado'] > cd['previsao_manha'] else "inverse"
                    st.metric(
                        cd['nome'],
                        f"{format_number(cd['liberado'])} kt",
                        delta=f"{format_number(cd['previsao_manha'])} kt previsto",
                        delta_color=delta_color
                    )
    
    else:
        # VISÃO EXPANDIDA - COM FONTE MENOR E 2 CASAS DECIMAIS
        st.markdown("#### 📊 Planilha Completa de Despacho")
        
        # CSS para fontes menores nos containers
        st.markdown("""
        <style>
        .small-metric .stMetric {
            font-size: 0.8rem !important;
        }
        .small-metric .stMetric label {
            font-size: 0.7rem !important;
        }
        .small-metric .stMetric value {
            font-size: 0.9rem !important;
        }
        .compact-container {
            padding: 0.5rem !important;
            margin-bottom: 0.5rem !important;
        }
        .compact-container .stMetric {
            margin-bottom: 0.2rem !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Total Geral
        st.markdown("##### **TOTAL GERAL**")
        with st.container(border=True):
             # Acumulado em linha separada
            st.markdown("**HOJE**", help="Dados do dia atual")
            cols = st.columns(3)
            with cols[0]:
                st.metric("PLANO", f"{format_number(plano_data['total_geral']['hoje_plano'])} kt", 
                         help="Plano para hoje")
            with cols[1]:
                st.metric("LIBERADO", f"{format_number(plano_data['total_geral']['hoje_liberado'])} kt",
                         help="Quantidade liberada hoje")
            with cols[2]:
                st.metric("PLANO", f"{format_number(plano_data['total_geral']['dia_anterior_plano'])} kt",
                         help="Plano do dia anterior")

            # Acumulado em linha separada
            st.markdown("---")
            st.markdown("**DIA ANTERIOR**", help="Dados do dia anterior")
            cols = st.columns(2)
            with cols[0]:
                st.metric("REAL", f"{format_number(plano_data['total_geral']['dia_anterior_real'])} kt",
                         help="Realizado no dia anterior")
            with cols[1]:
                delta_color = "normal" if plano_data['total_geral']['dia_anterior_delta'] >= 0 else "inverse"
                st.metric("∆", f"{format_number(plano_data['total_geral']['dia_anterior_delta'])} kt", 
                         delta_color=delta_color,
                         help="Diferença entre real e plano do dia anterior")

            # Acumulado em linha separada
            st.markdown("---")
            st.markdown("**MENSAL**", help="Dados do mês")
            acum_cols = st.columns(3)
            with acum_cols[0]:
                st.metric("PLANO ACUM.", f"{format_number(plano_data['total_geral']['acumulado_plano'])} kt",
                         help="Plano acumulado")
            with acum_cols[1]:
                st.metric("REAL ACUM.", f"{format_number(plano_data['total_geral']['acumulado_real'])} kt",
                         help="Real acumulado")
            with acum_cols[2]:
                delta_color = "normal" if plano_data['total_geral']['acumulado_delta'] >= 0 else "inverse"
                st.metric("∆ ACUM", f"{format_number(plano_data['total_geral']['acumulado_delta'])} kt", 
                         delta_color=delta_color,
                         help="Diferença acumulada")
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Clientes Diretos - Detalhado
        st.markdown("##### 🏭 CLIENTES DIRETOS - DETALHADO")
        
        # Total Clientes Diretos - Layout mais compacto
        with st.container(border=True):
            st.markdown('<div class="compact-container">', unsafe_allow_html=True)
            total = plano_data['clientes_diretos']['total']
            
            # Primeira linha - principais indicadores
            linha1_cols = st.columns(5)
            with linha1_cols[0]:
                st.metric("PREV.", f"{format_number(total['previsao_manha'])} kt",
                         help="Previsão da manhã")
            with linha1_cols[1]:
                st.metric("PLANO", f"{format_number(total['plano'])} kt",
                         help="Plano do dia")
            with linha1_cols[2]:
                st.metric("LIB.", f"{format_number(total['liberado'])} kt",
                         help="Liberado hoje")
            with linha1_cols[3]:
                st.metric("D.ANT REAL", f"{format_number(total['dia_anterior_real'])} kt",
                         help="Dia anterior - Real")
            with linha1_cols[4]:
                delta_color = "normal" if total['dia_anterior_delta'] >= 0 else "inverse"
                st.metric("∆ D.ANT", f"{format_number(total['dia_anterior_delta'])} kt", 
                         delta_color=delta_color,
                         help="Delta dia anterior")
            
            # Segunda linha - acumulados
            linha2_cols = st.columns(4)
            with linha2_cols[0]:
                st.metric("ACUM PLANO", f"{format_number(total['acumulado_plano'])} kt",
                         help="Acumulado plano")
            with linha2_cols[1]:
                st.metric("ACUM REAL", f"{format_number(total['acumulado_real'])} kt",
                         help="Acumulado real")
            with linha2_cols[2]:
                delta_color = "normal" if total['acumulado_delta'] >= 0 else "inverse"
                st.metric("∆ ACUM", f"{format_number(total['acumulado_delta'])} kt", 
                         delta_color=delta_color,
                         help="Delta acumulado")
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Usinas - Layout mais compacto
        st.markdown("**USINAS**")
        total_usinas = sum(usina['liberado'] for usina in plano_data['clientes_diretos']['usinas'])
        with st.container(border=True):
            st.markdown('<div class="compact-container">', unsafe_allow_html=True)
            st.metric("TOTAL USINAS", f"{format_number(total_usinas)} kt",
                     help="Total liberado das usinas")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Detalhes das Usinas - Layout horizontal compacto
        for usina in plano_data['clientes_diretos']['usinas']:
            with st.container(border=True):
                st.markdown('<div class="compact-container">', unsafe_allow_html=True)
                st.markdown(f"**{usina['nome']}**")
                
                # Layout com 2 linhas de métricas
                linha1_cols = st.columns(4)
                with linha1_cols[0]:
                    st.metric("PREV", f"{format_number(usina['previsao_manha'])} kt")
                with linha1_cols[1]:
                    st.metric("PLANO", f"{format_number(usina['plano'])} kt")
                with linha1_cols[2]:
                    st.metric("LIB", f"{format_number(usina['liberado'])} kt")
                with linha1_cols[3]:
                    st.metric("D.ANT", f"{format_number(usina['dia_anterior_real'])} kt")
                
                linha2_cols = st.columns(4)
                with linha2_cols[0]:
                    delta_color = "normal" if usina['dia_anterior_delta'] >= 0 else "inverse"
                    st.metric("∆ D.ANT", f"{format_number(usina['dia_anterior_delta'])} kt", delta_color=delta_color)
                with linha2_cols[1]:
                    st.metric("ACUM P", f"{format_number(usina['acumulado_plano'])} kt")
                with linha2_cols[2]:
                    st.metric("ACUM R", f"{format_number(usina['acumulado_real'])} kt")
                with linha2_cols[3]:
                    delta_color = "normal" if usina['acumulado_delta'] >= 0 else "inverse"
                    st.metric("∆ ACUM", f"{format_number(usina['acumulado_delta'])} kt", delta_color=delta_color)
                
                st.markdown('</div>', unsafe_allow_html=True)
        
        # CDs - Layout mais compacto
        st.markdown("**CENTROS DE DISTRIBUIÇÃO**")
        total_cds = sum(cd['liberado'] for cd in plano_data['clientes_diretos']['cds'])
        with st.container(border=True):
            st.markdown('<div class="compact-container">', unsafe_allow_html=True)
            st.metric("TOTAL CDs", f"{format_number(total_cds)} kt",
                     help="Total liberado dos CDs")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Detalhes dos CDs - Layout horizontal compacto
        for cd in plano_data['clientes_diretos']['cds']:
            with st.container(border=True):
                st.markdown('<div class="compact-container">', unsafe_allow_html=True)
                st.markdown(f"**{cd['nome']}**")
                
                # Layout com 2 linhas de métricas
                linha1_cols = st.columns(4)
                with linha1_cols[0]:
                    st.metric("PREV", f"{format_number(cd['previsao_manha'])} kt")
                with linha1_cols[1]:
                    st.metric("PLANO", f"{format_number(cd['plano'])} kt")
                with linha1_cols[2]:
                    st.metric("LIB", f"{format_number(cd['liberado'])} kt")
                with linha1_cols[3]:
                    st.metric("D.ANT", f"{format_number(cd['dia_anterior_real'])} kt")
                
                linha2_cols = st.columns(4)
                with linha2_cols[0]:
                    delta_color = "normal" if cd['dia_anterior_delta'] >= 0 else "inverse"
                    st.metric("∆ D.ANT", f"{format_number(cd['dia_anterior_delta'])} kt", delta_color=delta_color)
                with linha2_cols[1]:
                    st.metric("ACUM P", f"{format_number(cd['acumulado_plano'])} kt")
                with linha2_cols[2]:
                    st.metric("ACUM R", f"{format_number(cd['acumulado_real'])} kt")
                with linha2_cols[3]:
                    delta_color = "normal" if cd['acumulado_delta'] >= 0 else "inverse"
                    st.metric("∆ ACUM", f"{format_number(cd['acumulado_delta'])} kt", delta_color=delta_color)
                
                st.markdown('</div>', unsafe_allow_html=True)