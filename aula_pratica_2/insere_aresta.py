# insereAresta(matriz, vi, vj)
# Descrição: Insere uma aresta no grafo considerando o par de vértices vi e vj.
# Entrada: matriz de adjacências, vi e vj (ambos são números inteiros que indicam o id do vértice)
# Saída: matriz de adjacências (tipo numpy.ndarray) com a aresta inserida.

def  insereAresta(matriz, vi, vj):
    matriz[vi][vj] = 1
    matriz[vj][vi] = 1
    print(matriz)

matriz = [[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]]
insereAresta(matriz, 0, 2)