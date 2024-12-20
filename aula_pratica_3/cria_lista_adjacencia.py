# Descrição: Cria uma lista de adjacências de um grafo representado por uma matriz de adjacências.
# Entrada: matriz de adjacências (arquivo .txt)
# Saída: lista de adjacências (tipo Dictionary)

import numpy as np

def criaListaAdjacencias(matriz):
    # Verifica se a matriz é quadrada
    if matriz.shape[0] != matriz.shape[1]:
        raise ValueError("A matriz de adjacências deve ser quadrada.")
    
    # Inicializa a lista de adjacências como um dicionário
    listaAdj = {}
    
    # Percorre cada vértice (linha da matriz)
    for i in range(matriz.shape[0]):
        # Lista de vizinhos para o vértice i
        vizinhos = []
        for j in range(matriz.shape[1]):
            if matriz[i, j] > 0:  # Se houver uma aresta, adiciona o vizinho
                vizinhos.append(j)
        listaAdj[i] = vizinhos  # Associa o vértice à sua lista de vizinhos

    return listaAdj

def carregarMatrizDeArquivo(caminho):
    with open(caminho, 'r') as arquivo:
        matriz = [list(map(int, linha.split())) for linha in arquivo]
    return np.array(matriz)

# Caminho para o arquivo
arquivo = './dados/ponte.txt'

# Criando a lista de adjacências
listaAdj = criaListaAdjacencias(arquivo)

print("Lista de adjacências:")
print(listaAdj)