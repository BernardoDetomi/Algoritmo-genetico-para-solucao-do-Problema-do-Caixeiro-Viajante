# 🧬 Algoritmo Genético para o Problema do Caixeiro Viajante (TSP)

Este repositório contém a implementação de um **Algoritmo Genético (AG)** para resolver o **Problema do Caixeiro Viajante (TSP - Traveling Salesman Problem)**. O código utiliza matrizes de distâncias fornecidas em arquivos de texto para encontrar a rota ótima.

## 🗂️ Estrutura de Arquivos

- [` > main.py < `](./main.py): 🚀 Arquivo principal que executa o algoritmo genético, incluindo a leitura da matriz de distâncias e experimentos fatoriais.
- [` > algoritmo_genetico.py < `](./algoritmo_genetico.py): 💡 Implementação do núcleo do algoritmo genético, com seleção de pais, crossover, mutação, e critérios de parada por estagnação.
- [` > utils.py < `](./utils.py): 🔧 Funções utilitárias como cálculo de distância, criação de rotas, mutação e crossover.
- [` > matriz_distancias4.txt < `](./matriz_distancias4.txt) [` > matriz_distancias8.txt < `](./matriz_distancias8.txt) [` > matriz_distancias15.txt < `](./matriz_distancias15.txt): 📊 Arquivos de teste contendo matrizes de distâncias para diferentes números de cidades (4, 8 e 15 cidades, respectivamente).

## 📂 Pasta [`  testes  `](./testes)

Dentro da pasta [` > testes < `](./testes), você encontrará subpastas organizadas pelas seguintes instâncias de matriz de distâncias:

- [` > matriz_distancias4.txt < `](./matriz_distancias4.txt): 🔢 Contém testes com matrizes de distâncias de 4 cidades.
- [` > matriz_distancias8.txt < `](./matriz_distancias8.txt): 🔢 Contém testes com matrizes de distâncias de 8 cidades.
- [` > matriz_distancias15.txt < `](./matriz_distancias15.txt): 🔢 Contém testes com matrizes de distâncias de 15 cidades.

Cada subpasta armazena os resultados dos experimentos para a respectiva matriz.

## 🚀 Como Executar o Código

1. Escolha a matriz de distâncias desejada (por exemplo, [` > matriz_distancias4.txt < `](./matriz_distancias4.txt) [` > matriz_distancias8.txt < `](./matriz_distancias8.txt) ou [` > matriz_distancias15.txt < `](./matriz_distancias15.txt)).
2. Salve a matriz de distâncias no arquivo `matriz_distancias.txt` ou ajuste o caminho no código.
3. Execute o programa com o seguinte comando:
   ```bash
   python main.py

## 🔧 Ajuste de Parâmetros

No arquivo [` > main.py < `](./main.py), você pode ajustar os seguintes parâmetros para os experimentos:  

- Tamanho da população: Controle o número de indivíduos na população, variando entre valores como 50, 100, ou 200.
- Taxa de mutação: Defina a probabilidade de ocorrer mutação em uma rota, comumente ajustada entre 0.01 e 0.1.
- Taxa de crossover: Defina a probabilidade de ocorrer crossover entre dois pais, geralmente ajustada entre 0.7 e 0.9.

Esses parâmetros podem ser ajustados diretamente no código ou através da criação de novas instâncias de teste.

## 📊 Exemplo de Resultados

Os resultados de cada teste são armazenados automaticamente na pasta [` > testes < `](./testes). O nome dos arquivos reflete os parâmetros usados no teste, como o tamanho da população, a taxa de mutação e a taxa de crossover.

Exemplo de saída de resultado em console:

População: 100, Mutação: 0.01, Cruzamento: 0.8  
Melhor distância: 128  
Melhor rota: [0, 1, 3, 2, 0]  

Esses resultados podem ser encontrados nos arquivos gerados dentro das subpastas da pasta [` > testes < `](./testes).
