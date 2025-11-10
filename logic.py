from data import PLANO_DESPACHO_DATA
# logic.py
def generate_response(question: str) -> str:
    q = (question or "").lower()

    # NOVAS PERGUNTAS IMPLEMENTADAS
    if any(k in q for k in ["capacidade de 30t", "30t saindo de ipatinga", "ipatinga para grande bh", "grande belo horizonte"]):
        return (
            "🚚 **AALBORG**\n"
            "• Material liberado: 19,5t\n"
            "• **Sugestão:** Solicitar liberação do material suspenso por motivo comercial (9,2t) para composição de carga.\n"
            "• **Responsável:** Felipe Marques\n\n"
            "📦 **TIBERINAMG**\n"
            "• **Sugestão:** Avaliar antecipação de material (48t) com entrega programada para o próximo decêndio.\n"
            "• **Responsável:** Airam Tomas\n\n"
            "🔄 **Transferência para TISL**\n"
            "• **Sugestão:** Clientes ASSO (17t) e FERROMINAS (11t) com material disponível para transferência para TISL (Santa Luzia)\n"
            "• **Responsável:** Claudio Tadeu\n\n"
            "💡 **Recomendação:** Priorizar a solicitação de liberação do material suspenso da AALBORG para atender rapidamente à capacidade de 30t."
        )

    if any(k in q for k in ["672934-3", "ordem de venda 672934-3", "6t crítica", "composição de carga"]):
        return (
            "📋 **Ordem de Venda 672934-3**\n"
            "• **Cliente:** HONDASU\n"
            "• **Destino:** TAUBATÉ (Soluções Usiminas)\n"
            "• **Modal:** Ferroviário\n"
            "• **Situação:** CRÍTICA (6t)\n\n\n"
            "🚅 **Mantendo o modal como Ferroviário:**\n"
            "• Utilizar lote **0000170707** (12.0t) ou **0000234209** (8.5t) do próprio cliente (HONDASU)\n"
            "• **Total disponível:** 26.5t\n"
            "• **Vantagem:** Mantém a eficiência do modal ferroviário\n\n"
            "🚚 **Alternativa - Alterando para modal Rodoviário:**\n"
            "• Utilizar lotes da ordem **670005-3** (cliente MANSU - também crítica):\n"
            "  - Lote **0000226989** (9,6t)\n"
            "  - Lote **0000225760** (8,9t)\n"
            "• **Total disponível:** 24,5t\n"
            "• **Vantagem:** Agilidade no despacho\n\n"
            "⚡ **Recomendação:** Utilizar os lotes do próprio cliente HONDASU mantendo o modal ferroviário para melhor eficiência operacional."
        )

    # PERGUNTAS EXISTENTES (mantidas da versão anterior)
    if any(k in q for k in ["plano", "despacho", "planilha", "clientes diretos"]):
        total_liberado = PLANO_DESPACHO_DATA['total_geral']['hoje_liberado']
        acumulado_real = PLANO_DESPACHO_DATA['total_geral']['acumulado_real']
        acumulado_delta = PLANO_DESPACHO_DATA['total_geral']['acumulado_delta']
        
        # Calcular totais por categoria
        total_usinas = sum(usina['liberado'] for usina in PLANO_DESPACHO_DATA['clientes_diretos']['usinas'])
        total_cds = sum(cd['liberado'] for cd in PLANO_DESPACHO_DATA['clientes_diretos']['cds'])
        
        return (
            "📊 **Análise do Plano de Despacho Atual:**\n\n"
            f"• **Hoje liberado:** {total_liberado} kt\n"
            f"• **Acumulado real:** {acumulado_real} kt\n"
            f"• **Δ vs plano:** {acumulado_delta} kt {'(positivo)' if acumulado_delta >= 0 else '(negativo)'}\n\n"
            "🏭 **Distribuição por Origem:**\n"
            f"• **Usinas:** {total_usinas} kt ({total_usinas/total_liberado*100:.1f}%)\n"
            f"• **CDs:** {total_cds} kt ({total_cds/total_liberado*100:.1f}%)\n\n"
            "🚛 **Principais Origem:**\n"
            f"• **IPATINGA:** {PLANO_DESPACHO_DATA['clientes_diretos']['usinas'][0]['liberado']} kt\n"
            f"• **CUBATÃO:** {PLANO_DESPACHO_DATA['clientes_diretos']['usinas'][1]['liberado']} kt\n"
            f"• **TISL:** {PLANO_DESPACHO_DATA['clientes_diretos']['cds'][1]['liberado']} kt\n\n"
            "Deseja que eu detalhe alguma área específica do plano?"
        )

    if any(k in q for k in ["prioridade", "urgente", "crítica", "critica"]):
        return (
            "Identifiquei 2 despachos de prioridade CRÍTICA para hoje:\n\n"
            "1. OV 670103-15 - Construtora São Paulo (Laminado a Quente, 45 ton)\n"
            "2. OV 670105-08 - Indústria Mineira (Laminado a Quente, 28 ton)\n\n"
            "Recomendo programar estes despachos para as primeiras rotas do dia. "
            "Deseja que eu prepare a ordem de carregamento?"
        )

    if any(k in q for k in ["rota", "caminhão", "caminhao", "modal"]):
        return (
            "Analisando os modais de transporte disponíveis:\n\n"
            "• Modal Rodoviário: 2 despachos (73 ton)\n"
            "  - CAM-012: SP (45 ton)\n"
            "  - CAM-015: MG (28 ton)\n\n"
            "• Modal Ferroviário: 2 despachos (82 ton)\n"
            "  - CAM-008: RJ (32 ton)\n"
            "  - CAM-021: PR (50 ton)\n\n"
            "Tempo estimado de carregamento: 3-4 horas. Todos os veículos estão disponíveis."
        )

    if any(k in q for k in ["capacidade", "carga"]):
        return (
            "Capacidade atual: 78% utilizada\n\n"
            "• Capacidade total mensal: 4.620 ton\n"
            "• Já despachado: 3.420 ton\n"
            "• Meta do plano: 3.600 ton\n"
            "• Desvio: -180 ton (4,8% abaixo da meta)\n\n"
            "Precisamos acelerar os despachos para atingir a meta mensal. "
            "Há alguma demanda que possamos priorizar?"
        )

    if any(k in q for k in ["estoque", "disponível", "disponivel"]):
        return (
            "Status do estoque de Laminado a Quente:\n\n"
            "• Linha 1: 325 ton disponíveis\n"
            "• Linha 2: 285 ton disponíveis\n"
            "• Linha 3: 140 ton disponíveis\n"
            "• Linha 4: 400 ton disponíveis\n\n"
            "Todo o material tem estoque suficiente para os despachos planejados. "
            "Deseja verificar alguma linha específica?"
        )

    if any(k in q for k in ["relatório", "relatorio", "resumo", "desempenho"]):
        return (
            "Resumo do desempenho:\n\n"
            "📊 Dia Anterior: 156 ton\n"
            "📈 Acumulado Mensal: 3.420 ton\n"
            "🎯 Plano Acumulado: 3.600 ton\n"
            "⚠️ Desvio: -180 ton (95% da meta)\n\n"
            "Temos 4 pedidos liberados aguardando despacho e sugestão de plano para hoje "
            "com 4 despachos prioritários. Deseja revisar o plano?"
        )

    return (
        "Entendi sua solicitação. Com base nos dados atuais, posso ajudar com:\n\n"
        "• Análise de despachos e metas\n"
        "• Otimização de rotas e alocação de veículos\n"
        "• Verificação de estoque disponível\n"
        "• Acompanhamento de pedidos liberados\n\n"
        "Poderia especificar melhor o que precisa?"
    )