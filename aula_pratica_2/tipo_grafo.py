#  tipoGrafo(matriz)
# Descrição: Retorna o tipo do grafo representado por uma dada matriz de adjacências.
# Entrada: matriz de adjacências
# Saída: Integer (0 – simples; 1 – dígrafo; 20 – multigrafo; 21 – multigrafo dirigido; 30 – pseudografo; 31 – pseudografo dirigido)

import numpy as np

def tipoGrafo(matriz):
    # Verifica se é uma matriz quadrada
    if matriz.shape[0] != matriz.shape[1]:
        raise ValueError("A matriz de adjacência deve ser quadrada.")
    
    # Grafo dirigido (dígrafo) se matriz não é simétrica
    eh_dirigido = not np.array_equal(matriz, matriz.T)
    
    # Verifica se possui laços (valores na diagonal principal > 0)
    possui_laco = np.any(np.diag(matriz) > 0)
    
    # Verifica se é um multigrafo (valores maiores que 1 fora da diagonal)
    eh_multigrafo = np.any(matriz > 1)
    
    # Determina o tipo de grafo com base nas condições
    if possui_laco:
        if eh_dirigido:
            return 31  # Pseudografo dirigido
        return 30  # Pseudografo
    elif eh_multigrafo:
        if eh_dirigido:
            return 21  # Multigrafo dirigido
        return 20  # Multigrafo
    else:
        if eh_dirigido:
            return 1  # Dígrafo
        return 0  # Simples
    
# Matrizes de exemplo
matriz_simples = np.array([
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
])

matriz_digrafo = np.array([
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0]
])

matriz_multigrafo = np.array([
    [0, 2, 1],
    [2, 0, 1],
    [1, 1, 0]
])

matriz_pseudografo = np.array([
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
])

# Testando os tipos de grafo
print("Simples:", tipoGrafo(matriz_simples))  # Deve retornar 0
print("Dígrafo:", tipoGrafo(matriz_digrafo))  # Deve retornar 1
print("Multigrafo:", tipoGrafo(matriz_multigrafo))  # Deve retornar 20
print("Pseudografo:", tipoGrafo(matriz_pseudografo))  # Deve retornar 30