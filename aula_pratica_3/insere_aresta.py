# Descrição: Insere uma aresta no grafo considerando o par de vértices vi e vj.
# Entrada: lista de adjacências (tipo Dictionary), vi e vj (ambos são números inteiros que indicam o id do vértice)
# Saída: lista de adjacências (tipo Dictionary) com a aresta inserida.

def insereAresta(listaAdj, vi, vj):
    return

insereAresta({0: [1], 1: [0, 2, 3], 2: [1, 3], 3: [1, 2]}, 0, 2)

print('\n{0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], 3: [1, 2]}')