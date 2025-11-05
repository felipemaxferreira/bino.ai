# logic.py
def generate_response(question: str) -> str:
    q = (question or "").lower()

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