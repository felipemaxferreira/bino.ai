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
        "Crítica": ("#FEE2E2", "#B91C1C"),
        "Média": ("#FEF3C7", "#B45309"),
        "Baixa": ("#F3F4F6", "#374151")
    }
    bg, fg = colors.get(style, ("#F3F4F6", "#374151"))
    return f'<span style="font-size:.75rem; padding:.15rem .5rem; border-radius:999px; background:{bg}; color:{fg}; font-weight:600">{style}</span>'

def chip(text: str, color="#16A34A", bg="#ECFDF5"):
    return f'<span style="font-size:.75rem; padding:.15rem .5rem; border-radius:999px; background:{bg}; color:{color}; font-weight:600">{text}</span>'

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
                        {chip(s['modal'], color="#2563EB", bg="#EFF6FF") if s['modal']=='Ferroviário' else chip(s['modal'], color="#2563EB", bg="#EFF6FF")}
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


def assistant_header(title: str, subtitle: str, avatar_path: str):
    """
    Cabeçalho do assistente com avatar carregado de arquivo local (assets/Bino-Linkedin.jpg)
    usando st.image (mais robusto no Streamlit).
    """
    container = st.container()
    with container:
        col_avatar, col_text = st.columns([0.18, 0.82])
        with col_avatar:
            p = Path(avatar_path)
            if p.exists():
                # borda verde simulada com container + background
                st.markdown(
                    """
                    <div style="width:52px;height:52px;border-radius:50%;
                         border:2px solid #16A34A; overflow:hidden; box-shadow:0 1px 2px rgba(0,0,0,.08);">
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                # usa o mesmo espaço do div acima, mas renderiza a imagem logo abaixo
                st.image(str(p), width=52)
            else:
                # fallback discreto
                st.markdown(
                    """
                    <div style="width:52px;height:52px;border-radius:50%;
                         border:2px solid #16A34A;background:#E5E7EB"></div>
                    """,
                    unsafe_allow_html=True
                )
        with col_text:
            st.markdown(f"**{title}**")
            st.markdown('<span style="color:#16A34A; font-size:0.9rem;">Online — Pronto para ajudar</span>',
                        unsafe_allow_html=True)


# -------------------------------------------------
# 1) CSS Global seguro e responsivo (escopado p/ chat)
# -------------------------------------------------
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

    /* Área de mensagens com scroll */
    .bino-messages-container {
        height: 400px;
        overflow-y: auto;
        padding: 20px;
        background: #F8FAFC;
        display: flex;
        flex-direction: column;
        gap: 16px;
    }

    /* Estilos das mensagens */
    .bino-message {
        display: flex;
        gap: 12px;
        align-items: flex-start;
    }

    .bino-message.user {
        justify-content: flex-end;
    }

    .bino-message.user .bino-message-bubble {
        background: #16A34A;
        color: white;
        border-radius: 18px 18px 4px 18px;
    }

    .bino-message.assistant .bino-message-bubble {
        background: white;
        color: #111827;
        border: 1px solid #E5E7EB;
        border-radius: 18px 18px 18px 4px;
    }

    .bino-message-bubble {
        padding: 12px 16px;
        max-width: 70%;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
        line-height: 1.4;
    }

    .bino-message-timestamp {
        font-size: 0.75rem;
        color: #6B7280;
        margin-top: 4px;
    }
                
    .user-message-timestamp {
        font-size: 0.75rem;
        color: white;
        margin-top: 4px;
    }

    .bino-avatar {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        border: 2px solid #16A34A;
        object-fit: cover;
        flex-shrink: 0;
    }

    /* Quick actions */
    .bino-quick-actions {
        padding: 16px 20px;
        border-top: 1px solid #E5E7EB;
        background: white;
    }

    .bino-quick-actions .stButton > button {
        border: 1px solid #D1D5DB !important;
        background: #FFFFFF !important;
        color: #374151 !important;
        font-size: 0.85rem !important;
        padding: 6px 12px !important;
        border-radius: 16px !important;
        transition: all 0.2s ease !important;
        margin: 2px !important;
    }

    .bino-quick-actions .stButton > button:hover {
        border-color: #16A34A !important;
        color: #065F46 !important;
        background: #F0FDF4 !important;
        transform: translateY(-1px);
    }

    /* Área de input */
    .bino-input-container {
        padding: 16px 20px;
        background: white;
        border-top: 1px solid #E5E7EB;
    }

    /* Animação de digitação */
    .bino-typing {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        color: #065F46;
        font-style: italic;
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
    .bino-messages-container::-webkit-scrollbar {
        width: 6px;
    }

    .bino-messages-container::-webkit-scrollbar-track {
        background: #F1F5F9;
    }

    .bino-messages-container::-webkit-scrollbar-thumb {
        background: #CBD5E1;
        border-radius: 3px;
    }

    /* Responsividade */
    @media (max-width: 768px) {
        .bino-message-bubble {
            max-width: 85%;
        }
        
        .bino-messages-container {
            height: 350px;
        }
    }
    </style>
    """, unsafe_allow_html=True)
# -------------------------------------------------
# 2) Header do chat com avatar (usa st.image, robusto)
# -------------------------------------------------
def assistant_header(title: str, subtitle: str, avatar_path: str):
    """
    Cabeçalho do chat com avatar carregado de arquivo local (ex.: assets/Bino-Linkedin.jpg)
    """
    left, right = st.columns([0.12, 0.88])
    with left:
        p = Path(avatar_path)
        if p.exists():
            st.image(str(p), width=48, caption=None)
        else:
            # Placeholder discreto
            st.markdown(
                "<div style='width:48px;height:48px;border-radius:50%;border:2px solid #16A34A;background:#E5E7EB'></div>",
                unsafe_allow_html=True
            )
    with right:
        st.markdown(f"<div class='bino-chat-title'>{title}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='bino-chat-sub'>{subtitle}</div>", unsafe_allow_html=True)

# -----------------------------
# Avatar / header
# -----------------------------
def assistant_header(title: str, subtitle: str, avatar_path: str):
    """Cabeçalho do chat com avatar."""
    img_html = ""
    p = Path(avatar_path)
    if p.exists():
        img_html = f'<img src="app://{p.as_posix()}" style="width:42px;height:42px;border-radius:50%;border:2px solid #16A34A;object-fit:cover;" />'
    else:
        img_html = '<div style="width:42px;height:42px;border-radius:50%;border:2px solid #16A34A;background:#E5E7EB"></div>'

    st.markdown(
        f"""
        <div class="bino-chat-header">
            {img_html}
            <div>
                <div class="bino-chat-title">{title}</div>
                <div class="bino-chat-sub">{subtitle}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# -----------------------------
# Renderização de mensagens
# -----------------------------
def render_assistant_message(text: str, ts: str, avatar_path: str):
    p = Path(avatar_path)
    if p.exists():
        avatar_tag = f'<img class="bino-avatar" src="app://{p.as_posix()}" />'
    else:
        avatar_tag = '<div class="bino-avatar"></div>'
    st.markdown(
        f"""
        <div class="bino-msg assistant">
            {avatar_tag}
            <div>
              <div class="bino-bubble assistant">{text}</div>
              <div class="bino-ts">{ts}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_user_message(text: str, ts: str):
    st.markdown(
        f"""
        <div class="bino-msg user">
            <div>
              <div class="bino-bubble user">{text}</div>
              <div class="bino-ts" style="text-align:right">{ts}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_typing(avatar_path: str, label: str = "Bino está digitando"):
    p = Path(avatar_path)
    if p.exists():
        avatar_tag = f'<img class="bino-avatar" src="app://{p.as_posix()}" />'
    else:
        avatar_tag = '<div class="bino-avatar"></div>'

    st.markdown(
        f"""
        <div class="bino-msg assistant">
            {avatar_tag}
            <div class="bino-bubble assistant" style="display:inline-flex;align-items:center;gap:10px;">
                <span class="bino-typing">{label}</span>
                <span class="bino-dot"></span><span class="bino-dot"></span><span class="bino-dot"></span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )