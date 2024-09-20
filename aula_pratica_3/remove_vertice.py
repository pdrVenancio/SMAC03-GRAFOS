# Descrição: Remove um vértice do grafo.
# Entrada: lista de adjacências (tipo Dictionary), vi (número inteiro que indica o id do vértice)
# Saída: lista de adjacências (tipo Dictionary) com o vértice removido.

def removeVertice(listaAdj, vi):
    return

removeVertice({0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], 3: [1, 2]}, 2)
print('\n{0: [1], 1: [0, 3], 3: [1]}')