# Algoritmo Genético para o Problema do Caixeiro Viajante

Este repositório contém uma implementação de um Algoritmo Genético (AG) para resolver o Problema do Caixeiro Viajante (TSP - Traveling Salesman Problem). A implementação segue os passos definidos em um fluxograma e utiliza uma instância de matriz de distâncias fornecida em um arquivo de texto.

## Estrutura de Arquivos

- `main.py`: Executa o algoritmo genético, incluindo a leitura da matriz de distâncias e experimentos fatoriais.
- `algoritmo_genetico.py`: Implementa o núcleo do algoritmo genético, incluindo os critérios de parada por estagnação e convergência.
- `utils.py`: Contém funções utilitárias como cálculo de distância, criação de rotas, mutação e crossover.
- `matriz_distancias.txt`: Arquivo contendo a matriz de distâncias para o TSP (pode ser substituído por outro arquivo com formato compatível).

## Instâncias de Teste

Você pode utilizar instâncias como **LAU15** ou **SGB128**. Basta salvar o arquivo de distâncias no formato de matriz (um arquivo `.txt` ou `.csv`) e rodar o programa.

## Como Rodar

1. Salve a matriz de distâncias no arquivo `matriz_distancias.txt`.
2. Execute o arquivo `main.py`:
   ```bash
   python main.py
