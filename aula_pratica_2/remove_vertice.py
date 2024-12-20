# removeVertice(matriz, vi)
# Descrição: Remove um vértice do grafo.
# Entrada: matriz de adjacências, vi (número inteiro que indica o id do vértice)
# Saída: matriz de adjacências (tipo numpy.ndarray) com o vértice removido.

import numpy as np

def removeVertice(matriz, vi):
    if not (0 <= vi < matriz.shape[0]):
        raise ValueError("Índice do vértice inválido.")
    
    # Remove a linha e a coluna associadas ao vértice vi
    matriz = np.delete(matriz, vi, axis=0)  # Remove a linha
    matriz = np.delete(matriz, vi, axis=1)  # Remove a coluna
    
    return matriz

# Criando uma matriz de adjacência de exemplo
matriz = np.array([
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
])

# Removendo o vértice 1
nova_matriz = removeVertice(matriz, 1)

print("Matriz original:")
print(matriz)
print("\nNova matriz após remover o vértice 1:")
print(nova_matriz)