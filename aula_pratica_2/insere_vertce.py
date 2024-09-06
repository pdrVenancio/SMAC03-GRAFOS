# insereVertice(matriz, vi)
# Descrição: Insere um vértice no grafo.
# Entrada: matriz de adjacências, vi (número inteiro que indica o id do vértice)
# Saída: matriz de adjacências (tipo numpy.ndarray) com o vértice inserido

import numpy as np

def insereVertice(matriz):
    for item in matriz:
        item.append(0)
    matriz.append([0] * (len(matriz) + 1))
    print(np.array(matriz))

matriz = [[0,0,0],
          [0,0,0],
          [0,0,0],
        ]

insereVertice(matriz)