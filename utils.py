import random

def calcular_distancia(rota, matriz_distancias):
    distancia_total = 0
    for i in range(len(rota) - 1):
        distancia_total += matriz_distancias[rota[i]][rota[i + 1]]
    distancia_total += matriz_distancias[rota[-1]][rota[0]]
    return distancia_total

def criar_rota(num_cidades):
    rota = list(range(num_cidades))
    random.shuffle(rota)
    return rota

def criar_populacao(tamanho_populacao, num_cidades):
    return [criar_rota(num_cidades) for _ in range(tamanho_populacao)]

def selecionar_pais(populacao, fitness, tamanho_torneio):
    pais = []
    for _ in range(2):
        torneio = random.sample(list(enumerate(fitness)), tamanho_torneio)
        melhor = min(torneio, key=lambda x: x[1])
        pais.append(populacao[melhor[0]])
    return pais

def cruzamento(pai1, pai2):
    tamanho = len(pai1)
    filho = [None] * tamanho
    inicio, fim = sorted(random.sample(range(tamanho), 2))
    filho[inicio:fim] = pai1[inicio:fim]
    posicao_filho = fim
    for cidade in pai2:
        if cidade not in filho:
            if posicao_filho == tamanho:
                posicao_filho = 0
            filho[posicao_filho] = cidade
            posicao_filho += 1
    return filho

def mutacao(rota, taxa_mutacao):
    if random.random() < taxa_mutacao:
        i, j = random.sample(range(len(rota)), 2)
        rota[i], rota[j] = rota[j], rota[i]
    return rota