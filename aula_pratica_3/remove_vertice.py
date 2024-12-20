# Descrição: Remove um vértice do grafo.
# Entrada: lista de adjacências (tipo Dictionary), vi (número inteiro que indica o id do vértice)
# Saída: lista de adjacências (tipo Dictionary) com o vértice removido.

def removeVertice(listaAdj, vi):
    for v in listaAdj:
        if vi in listaAdj[v]:
            listaAdj[v].remove(vi)

    # Remove o vértice vi da lista de adjacências
    if vi in listaAdj:
        del listaAdj[vi]

    return listaAdj

# Lista de adjacências inicial
listaAdj = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
    3: [1]
}

# Remove o vértice 1
listaAdj = removeVertice(listaAdj, 1)

print("Lista de adjacências atualizada:")
print(listaAdj)
