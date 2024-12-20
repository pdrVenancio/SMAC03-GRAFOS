# Descrição: Insere um vértice no grafo.
# Entrada: lista de adjacências (tipo Dictionary), vi (número inteiro que indica o id do vértice)
# Saída: lista de adjacências (tipo Dictionary) com o vértice inserido.

def insereVertice(listaAdj, vi):
    # Verifica se o vértice já existe
    if vi not in listaAdj:
        listaAdj[vi] = []  # Adiciona o vértice sem vizinhos
    return listaAdj

# Lista de adjacências inicial
listaAdj = {
    0: [1, 2],
    1: [0],
    2: [0]
}

# Insere um novo vértice 3
listaAdj = insereVertice(listaAdj, 3)

print("Lista de adjacências atualizada:")
print(listaAdj)
