# Descrição: Insere uma aresta no grafo considerando o par de vértices vi e vj.
# Entrada: lista de adjacências (tipo Dictionary), vi e vj (ambos são números inteiros que indicam o id do vértice)
# Saída: lista de adjacências (tipo Dictionary) com a aresta inserida.

def insereAresta(listaAdj, vi, vj):
    # Adiciona o vértice vj na lista de vizinhos de vi
    if vi in listaAdj:
        if vj not in listaAdj[vi]:  # Evita duplicação
            listaAdj[vi].append(vj)
    else:
        listaAdj[vi] = [vj]

    # Adiciona o vértice vi na lista de vizinhos de vj (para grafos não direcionados)
    if vj in listaAdj:
        if vi not in listaAdj[vj]:  # Evita duplicação
            listaAdj[vj].append(vi)
    else:
        listaAdj[vj] = [vi]

    return listaAdj

# Lista de adjacências inicial
listaAdj = {
    0: [1, 2],
    1: [0],
    2: [0],
    3: []
}

# Insere uma aresta entre os vértices 1 e 3
listaAdj = insereAresta(listaAdj, 1, 3)

print("Lista de adjacências atualizada:")
print(listaAdj)
