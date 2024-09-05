import random
from utils import criar_populacao, calcular_distancia, selecionar_pais, cruzamento, mutacao

def algoritmo_genetico(matriz_distancias, tamanho_populacao=100, geracoes=500, taxa_mutacao=0.01, tamanho_torneio=5, max_estagnacao=50):
    num_cidades = len(matriz_distancias)
    populacao = criar_populacao(tamanho_populacao, num_cidades)
    melhor_fitness_geral = float('inf')
    estagnacao = 0
    
    for geracao in range(geracoes):
        fitness = [calcular_distancia(rota, matriz_distancias) for rota in populacao]
        nova_populacao = []

        # Seleção e reprodução
        for _ in range(tamanho_populacao // 2):
            pais = selecionar_pais(populacao, fitness, tamanho_torneio)
            filho1 = cruzamento(pais[0], pais[1])
            filho2 = cruzamento(pais[1], pais[0])
            nova_populacao.append(mutacao(filho1, taxa_mutacao))
            nova_populacao.append(mutacao(filho2, taxa_mutacao))

        populacao = nova_populacao

        melhor_rota = min(populacao, key=lambda rota: calcular_distancia(rota, matriz_distancias))
        melhor_distancia = calcular_distancia(melhor_rota, matriz_distancias)

        if melhor_distancia < melhor_fitness_geral:
            melhor_fitness_geral = melhor_distancia
            estagnacao = 0
        else:
            estagnacao += 1

        if estagnacao >= max_estagnacao:
            print(f"Parada por estagnação na geração {geracao + 1}")
            break

        print(f"Geração {geracao + 1}: Melhor distância = {melhor_distancia}")

    return melhor_rota, melhor_distancia