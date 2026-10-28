from simulation import Simulation

modelos_bateria = {
    0: {
        "nome": "LFP_40Ah",
        "quimica": "LFP",
        "capacidade_Ah": 40,
        "tensao_nominal_V": 3.2,
        "tensao_maxima_V": 3.65,
        "c_rate": 6,
        "preco_usd": 36.62,
        "volume_m3": 0.596,    #L, Volume da célula?
        "peso_kg": 1.085,       #kg
        "vida_ciclos": 4000,
        "SOC_inicial": 20,
    },
    1: {
        "nome": "LFP_60Ah",                 #Genérico para teste
        "quimica": "LFP",
        "capacidade_Ah": 60,
        "tensao_nominal_V": 3.2,
        "tensao_maxima_V": 3.65,
        "c_rate": 4,
        "preco_usd": 28.5,
        "volume_m3": 0.596,    #L
        "peso_kg": 1.5,       #kg
        "vida_ciclos": 2000,  
        "SOC_inicial": 20,
    },
    2: {
        "nome": "Na_50Ah",                 #Genérico para teste
        "quimica": "Na",
        "capacidade_Ah": 50,
        "tensao_nominal_V": 2.85,
        "tensao_maxima_V": 3.5,
        "c_rate": 0.5,
        "preco_usd": 27.5,
        "volume_m3": 0.596,    #L
        "peso_kg": 1.65,       #kg
        "vida_ciclos": 8000,  
        "SOC_inicial": 20,
    }
}

