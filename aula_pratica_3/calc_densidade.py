# Descrição: Retorna o valor da densidade do grafo.
# Entrada: lista de adjacências (tipo Dictionary)
# Saída: Float (valor da densidade com precisão de três casas decimais)

def calcDensidade(listaAdj):

    # Número de vértices
    n_vertices = len(listaAdj)
    
    # Calcula o número de arestas
    n_arestas = sum(len(vizinhos) for vizinhos in listaAdj.values()) / 2  # Dividir por 2 para grafos não direcionados
    
    # Se o número de vértices for menor ou igual a 1, a densidade é zero
    if n_vertices <= 1:
        return 0.0

    # Fórmula da densidade para grafos não direcionados
    densidade = (2 * n_arestas) / (n_vertices * (n_vertices - 1))

    return round(densidade, 3)

# Exemplo de lista de adjacências
listaAdj = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}

# Calcula a densidade
densidade = calcDensidade(listaAdj)
print("Densidade do grafo:", densidade)