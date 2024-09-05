import os
from datetime import datetime
from algoritmo_genetico import algoritmo_genetico
import numpy as np

def ler_matriz_distancias_txt(nome_arquivo):
    with open(nome_arquivo) as f:
        matriz = [list(map(int, linha.strip().split())) for linha in f]
    return np.array(matriz)

# Função para salvar os resultados em arquivos txt na pasta 'testes'
def salvar_resultados(tamanho_pop, taxa_mut, taxa_cruz, melhor_distancia, melhor_rota):
    # Criar a pasta 'testes' se não existir
    if not os.path.exists('testes'):
        os.makedirs('testes')

    # Gerar um nome único para o arquivo
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    nome_arquivo = f"testes/teste_{tamanho_pop}_{taxa_mut}_{taxa_cruz}_{timestamp}.txt"
    
    # Escrever os resultados no arquivo
    with open(nome_arquivo, 'w') as f:
        f.write(f"Populacao: {tamanho_pop}\n")
        f.write(f"Taxa de Mutacao: {taxa_mut}\n")
        f.write(f"Taxa de Cruzamento: {taxa_cruz}\n")
        f.write(f"Melhor Distancia: {melhor_distancia}\n")
        f.write(f"Melhor Rota: {melhor_rota}\n")
    
    print(f"Resultados salvos em: {nome_arquivo}")

if __name__ == "__main__":
    matriz_distancias = ler_matriz_distancias_txt("matriz_distancias8.txt")
    
    tamanhos_populacao = [50, 100, 200]
    taxas_mutacao = [0.01, 0.05, 0.1]
    taxas_cruzamento = [0.7, 0.8, 0.9]

    for tamanho_pop in tamanhos_populacao:
        for taxa_mut in taxas_mutacao:
            for taxa_cruz in taxas_cruzamento:
                print(f"\nPopulação: {tamanho_pop}, Mutação: {taxa_mut}, Cruzamento: {taxa_cruz}")
                melhor_rota, melhor_distancia = algoritmo_genetico(
                    matriz_distancias, 
                    tamanho_populacao=tamanho_pop, 
                    taxa_mutacao=taxa_mut, 
                    geracoes=500
                )
                print(f"Melhor distância: {melhor_distancia}")
                print(f"Melhor rota: {melhor_rota}")
                
                # Salvar os resultados no arquivo
                salvar_resultados(tamanho_pop, taxa_mut, taxa_cruz, melhor_distancia, melhor_rota)