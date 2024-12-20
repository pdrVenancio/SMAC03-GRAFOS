# Descrição: Remove uma aresta do grafo considerando o par de vértices vi e vj.
# Entrada: lista de adjacências (tipo Dictionary), vi e vj (ambos são números inteiros que indicam os ids dos vértices)
# Saída: lista de adjacências (tipo Dictionary) com a aresta removida.

def removeAresta(listaAdj, vi, vj):
    # Remove vj da lista de vizinhos de vi, se existir
    if vi in listaAdj and vj in listaAdj[vi]:
        listaAdj[vi].remove(vj)

    # Remove vi da lista de vizinhos de vj, se existir (para grafos não direcionados)
    if vj in listaAdj and vi in listaAdj[vj]:
        listaAdj[vj].remove(vi)

    return listaAdj

# Lista de adjacências inicial
listaAdj = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
    3: []
}

# Remove a aresta entre os vértices 1 e 2
listaAdj = removeAresta(listaAdj, 1, 2)

print("Lista de adjacências atualizada:")
print(listaAdj)

