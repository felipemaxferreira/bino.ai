# data.py
DESPACHO_DATA = {
    "diaAnterior": 156,
    "acumulMensal": 3420,
    "planoAcumul": 3600,
    "desvio": -180,
    "capacidadeUtilizada": 78
}

SUGESTOES_PLANO = [
    {"id": "670103-15", "cliente": "Construtora São Paulo", "produto": "Laminado a Quente",
     "quantidade": "45 ton", "prioridade": "Crítica", "destino": "São Paulo - SP",
     "modal": "Rodoviário", "caminhao": "CAM-012"},
    {"id": "670104-22", "cliente": "Metalúrgica Rio", "produto": "Laminado a Quente",
     "quantidade": "32 ton", "prioridade": "Média", "destino": "Rio de Janeiro - RJ",
     "modal": "Ferroviário", "caminhao": "CAM-008"},
    {"id": "670105-08", "cliente": "Indústria Mineira", "produto": "Laminado a Quente",
     "quantidade": "28 ton", "prioridade": "Crítica", "destino": "Belo Horizonte - MG",
     "modal": "Rodoviário", "caminhao": "CAM-015"},
    {"id": "670106-31", "cliente": "Fábrica Curitiba", "produto": "Laminado a Quente",
     "quantidade": "50 ton", "prioridade": "Baixa", "destino": "Curitiba - PR",
     "modal": "Ferroviário", "caminhao": "CAM-021"}
]

ESTOQUE_DATA = [
    {"produto": "Laminado a Quente", "estoque": 450, "reservado": 125, "disponivel": 325, "unidade": "ton"},
    {"produto": "Laminado a Quente", "estoque": 380, "reservado": 95, "disponivel": 285, "unidade": "ton"},
    {"produto": "Laminado a Quente", "estoque": 220, "reservado": 80, "disponivel": 140, "unidade": "ton"},
    {"produto": "Laminado a Quente", "estoque": 550, "reservado": 150, "disponivel": 400, "unidade": "ton"},
    {"produto": "Laminado a Quente", "estoque": 320, "reservado": 60, "disponivel": 260, "unidade": "ton"},
]

LIBERADO_DATA = [
    {"id": "670101-42", "cliente": "Construtora ABC", "produto": "Laminado a Quente",
     "quantidade": "35 ton", "dataLiberacao": "04/11/2025", "status": "Liberado"},
    {"id": "670102-18", "cliente": "Metalúrgica XYZ", "produto": "Laminado a Quente",
     "quantidade": "42 ton", "dataLiberacao": "04/11/2025", "status": "Liberado"},
    {"id": "670098-25", "cliente": "Indústria Delta", "produto": "Laminado a Quente",
     "quantidade": "28 ton", "dataLiberacao": "03/11/2025", "status": "Liberado"},
    {"id": "670107-09", "cliente": "Obras Beta", "produto": "Laminado a Quente",
     "quantidade": "55 ton", "dataLiberacao": "04/11/2025", "status": "Liberado"},
]