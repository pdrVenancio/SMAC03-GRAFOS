# Descrição: Verifica se os vértices vi e vj são adjacentes.
# Entrada: lista de adjacências (tipo Dictionary), vi e vj (ambos números inteiros que indica o id do vértice)
# Saída: Boolean (True se os vértices são adjacentes; False caso contrário) 

def verificaAdjacencia(listaAdj, vi, vj):
    # Verifica se vj está na lista de vizinhos de vi
    if vi in listaAdj and vj in listaAdj[vi]:
        return True
    return False

# Lista de adjacências
listaAdj = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
    3: [4],
    4: [3]
}

# Verifica se os vértices 0 e 1 são adjacentes
print(verificaAdjacencia(listaAdj, 0, 1))  # Resultado: True

# Verifica se os vértices 0 e 3 são adjacentes
print(verificaAdjacencia(listaAdj, 0, 3))  # Resultado: False