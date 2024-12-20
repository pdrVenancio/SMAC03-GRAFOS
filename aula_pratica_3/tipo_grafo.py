# Descrição: Retorna o tipo do grafo representado por uma dada lista de adjacências.
# Entrada: lista de adjacências (tipo Dictionary)
# Saída: Integer (0 – simples; 1 – dígrafo; 20 – multigrafo; 21 – multigrafo dirigido; 30 – pseudografo; 31 – pseudografo dirigido)

def tipoGrafo(listaAdj):
    eh_digrafo = False
    tem_loop = False
    tem_multiareste = False

    for vertice, vizinhos in listaAdj.items():
        # Verifica se é um dígrafo
        for vizinho in vizinhos:
            if vizinho not in listaAdj or vertice not in listaAdj[vizinho]:
                eh_digrafo = True

        # Verifica se há laços
        if vertice in vizinhos:
            tem_loop = True

        # Verifica se há multiarestas
        if len(set(vizinhos)) < len(vizinhos):
            tem_multiareste = True

    # Classifica o grafo com base nas verificações
    if tem_multiareste:
        if tem_loop:
            return 31 if eh_digrafo else 30
        return 21 if eh_digrafo else 20
    if tem_loop:
        return 31 if eh_digrafo else 30
    return 1 if eh_digrafo else 0

# Lista de adjacências de um grafo
listaAdj = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
    3: [3]  # Laço no vértice 3
}

tipo = tipoGrafo(listaAdj)
print(f"Tipo do grafo: {tipo}")
