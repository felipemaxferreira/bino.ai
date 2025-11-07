# data.py
DESPACHO_DATA = {
    "diaAnterior": 13.421,
    "acumulMensal": 46.941,
    "planoAcumul": 36.991,
    "desvio": 9.953,
    "capacidadeUtilizada": 82
}

# data.py - Atualize o PLANO_DESPACHO_DATA com os novos dados
PLANO_DESPACHO_DATA = {
    "hoje": "2025-09-04",
    "total_geral": {
        "hoje_plano": 17.50,
        "hoje_liberado": 15.32,
        "dia_anterior_plano": 8.5,
        "dia_anterior_real": 8.32,
        "dia_anterior_delta": -0.18,
        "acumulado_plano": 22.6,
        "acumulado_real": 21.71,
        "acumulado_delta": -0.89
    },
    "clientes_diretos": {
        "total": {
            "previsao_manha": 7.15,
            "previsao_tarde": 0,
            "plano": 8.1,
            "liberado": 15.32,
            "dia_anterior_plano": 8.5,
            "dia_anterior_real": 8.32,
            "dia_anterior_delta": -0.18,
            "acumulado_plano": 22.6,
            "acumulado_real": 21.71,
            "acumulado_delta": -0.89
        },
        "usinas": [
            {"nome": "IPATINGA", "previsao_manha": 3.2, "plano": 3.3, "liberado": 9.67, "dia_anterior_plano": 2.5, "dia_anterior_real": 2.71, "dia_anterior_delta": 0.21, "acumulado_plano": 7.1, "acumulado_real": 6.87, "acumulado_delta": -0.23},
            {"nome": "CUBATÃO", "previsao_manha": 1.8, "plano": 1.1, "liberado": 2.56, "dia_anterior_plano": 1.9, "dia_anterior_real": 2.11, "dia_anterior_delta": 0.21, "acumulado_plano": 5.0, "acumulado_real": 3.97, "acumulado_delta": -1.03},
            {"nome": "CABOTAGEM", "previsao_manha": 0.07, "plano": 1.0, "liberado": 0, "dia_anterior_plano": 0.06, "dia_anterior_real": 0.06, "dia_anterior_delta": 0.0, "acumulado_plano": 0.44, "acumulado_real": 0.44, "acumulado_delta": 0.0},
            {"nome": "CABOTAGEM SUL", "previsao_manha": 0, "plano": 0.5, "liberado": 0, "dia_anterior_plano": 0, "dia_anterior_real": 0, "dia_anterior_delta": 0.0, "acumulado_plano": 0.5, "acumulado_real": 0, "acumulado_delta": -0.5}
        ],
        "cds": [
            {"nome": "IMBIRUÇU", "previsao_manha": 0.2, "plano": 0.2, "liberado": 0.55, "dia_anterior_plano": 1.2, "dia_anterior_real": 0.76, "dia_anterior_delta": -0.44, "acumulado_plano": 2.41, "acumulado_real": 2.41, "acumulado_delta": 0.0},
            {"nome": "TISL", "previsao_manha": 0.5, "plano": 0.6, "liberado": 1.01, "dia_anterior_plano": 0.9, "dia_anterior_real": 0.7, "dia_anterior_delta": -0.2, "acumulado_plano": 1.5, "acumulado_real": 1.65, "acumulado_delta": 0.15},
            {"nome": "SUAPE", "previsao_manha": 10.2, "plano": 0.1, "liberado": 0.1, "dia_anterior_plano": 0.01, "dia_anterior_real": 0.01, "dia_anterior_delta": 0.0, "acumulado_plano": 0.25, "acumulado_real": 0.25, "acumulado_delta": 0.0},
            {"nome": "DFS RJ", "previsao_manha": 0.1, "plano": 0.2, "liberado": 0, "dia_anterior_plano": 0.7, "dia_anterior_real": 0.44, "dia_anterior_delta": -0.26, "acumulado_plano": 0.6, "acumulado_real": 0.74, "acumulado_delta": 0.14},
            {"nome": "DF CONFAB", "previsao_manha": 5.5, "plano": 0, "liberado": 0, "dia_anterior_plano": 0, "dia_anterior_real": 0, "dia_anterior_delta": 0.0, "acumulado_plano": 0, "acumulado_real": 0, "acumulado_delta": 0.0},
            {"nome": "TAUBATÉ", "previsao_manha": 3.2, "plano": 0, "liberado": 0, "dia_anterior_plano": 0.2, "dia_anterior_real": 0, "dia_anterior_delta": -0.2, "acumulado_plano": 0, "acumulado_real": 0, "acumulado_delta": 0.0},
            {"nome": "TESP", "previsao_manha": 0.24, "plano": 0.3, "liberado": 0.54, "dia_anterior_plano": 0.02, "dia_anterior_real": 0.39, "dia_anterior_delta": 0.37, "acumulado_plano": 1.19, "acumulado_real": 1.19, "acumulado_delta": 0.0},
            {"nome": "UTINGA", "previsao_manha": 0.48, "plano": 0.7, "liberado": 0.74, "dia_anterior_plano": 0.04, "dia_anterior_real": 0.49, "dia_anterior_delta": 0.45, "acumulado_plano": 0.5, "acumulado_real": 0.83, "acumulado_delta": 0.33},
            {"nome": "DFS SP", "previsao_manha": 0.2, "plano": 0.1, "liberado": 0, "dia_anterior_plano": 0.2, "dia_anterior_real": 0.14, "dia_anterior_delta": -0.06, "acumulado_plano": 0.2, "acumulado_real": 0.2, "acumulado_delta": 0.0},
            {"nome": "JSL", "previsao_manha": 0.44, "plano": 0, "liberado": 0.01, "dia_anterior_plano": 0, "dia_anterior_real": 0, "dia_anterior_delta": 0.0, "acumulado_plano": 0.53, "acumulado_real": 0.53, "acumulado_delta": 0.0},
            {"nome": "CDS SUL", "previsao_manha": 0.36, "plano": 0.2, "liberado": 0.14, "dia_anterior_plano": 0.7, "dia_anterior_real": 0.53, "dia_anterior_delta": -0.17, "acumulado_plano": 2.65, "acumulado_real": 2.65, "acumulado_delta": 0.0}
        ]
    }
}

# data.py - Atualize as SUGESTOES_PLANO baseadas na nova planilha
SUGESTOES_PLANO = [
    {"id": "670103-15", "cliente": "Toyota", "produto": "Laminado a Quente",
     "quantidade": "45 ton", "prioridade": "OV Crítica", "destino": "São Paulo - SP",
     "modal": "Rodoviário", "caminhao": "CAM-012", "usina": "IPATINGA"},
    {"id": "670104-22", "cliente": "Metalúrgica Rio", "produto": "Laminado a Frio",
     "quantidade": "32 ton", "prioridade": "Média", "destino": "Rio de Janeiro - RJ",
     "modal": "Ferroviário", "caminhao": "CAM-008", "usina": "CUBATÃO"},
    {"id": "670105-08", "cliente": "Honda Automóveis", "produto": "Laminado a Frio",
     "quantidade": "28 ton", "prioridade": "OV Crítica", "destino": "Belo Horizonte - MG",
     "modal": "Rodoviário", "caminhao": "CAM-015", "usina": "IPATINGA"},
    {"id": "670106-31", "cliente": "Convaço", "produto": "Laminado a Quente",
     "quantidade": "50 ton", "prioridade": "Baixa", "destino": "Curitiba - PR",
     "modal": "Ferroviário", "caminhao": "CAM-021", "usina": "CUBATÃO"},
    {"id": "670107-42", "cliente": "Indústria Mineira", "produto": "Chapa Grossa",
     "quantidade": "38 ton", "prioridade": "Média", "destino": "Uberlândia - MG",
     "modal": "Rodoviário", "caminhao": "CAM-025", "usina": "IPATINGA"}
]

ESTOQUE_DATA = [
    {"produto": "Laminado a Quente", "estoque": 450, "reservado": 125, "disponivel": 325, "unidade": "ton"},
    {"produto": "Laminado a Frio", "estoque": 380, "reservado": 95, "disponivel": 285, "unidade": "ton"},
    {"produto": "Chapa Grossa", "estoque": 220, "reservado": 80, "disponivel": 140, "unidade": "ton"},
    {"produto": "Laminado a Quente", "estoque": 550, "reservado": 150, "disponivel": 400, "unidade": "ton"},
    {"produto": "Laminado a Frio", "estoque": 320, "reservado": 60, "disponivel": 260, "unidade": "ton"},
]

LIBERADO_DATA = [
    {"id": "670101-42", "cliente": "Fiat", "produto": "Laminado a Quente",
     "quantidade": "35 ton", "dataLiberacao": "04/11/2025", "status": "Liberado"},
    {"id": "670102-18", "cliente": "Tiberina", "produto": "Laminado a Quente",
     "quantidade": "42 ton", "dataLiberacao": "04/11/2025", "status": "Liberado"},
    {"id": "670098-25", "cliente": "TT Steel", "produto": "Laminado a Quente",
     "quantidade": "28 ton", "dataLiberacao": "03/11/2025", "status": "Liberado"},
    {"id": "670107-09", "cliente": "Ternium", "produto": "Laminado a Quente",
     "quantidade": "55 ton", "dataLiberacao": "04/11/2025", "status": "Liberado"},
]