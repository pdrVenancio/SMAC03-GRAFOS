# Descrição: Remove uma aresta do grafo considerando o par de vértices vi e vj.
# Entrada: lista de adjacências (tipo Dictionary), vi e vj (ambos são números inteiros que indicam os ids dos vértices)
# Saída: lista de adjacências (tipo Dictionary) com a aresta removida.

def removeAresta(listaAdj, vi, vj):
    return

removeAresta({0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], 3: [1, 2]}, 0, 2)
print('\n{0: [1], 1: [0, 2, 3], 2: [1, 3], 3: [1, 2]}')