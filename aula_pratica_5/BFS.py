# BFS(listaAdj, v)
# Descrição: Busca em largura de um grafo retornando a sequência dos vértices visitados.
# Entrada: lista de adjacências (tipo Dictionary), id do vértice origem (tipo Int).
# Saída: sequência de vértices (tipo List)

def BFS(listaAdj, v):
    visitados = []
    visitados.append(v)
    analizado = []
    vertices_geral = []
    
    for i in listaAdj:
        vertices_geral.append(i)
    
    while len(visitados) != 0:
        v = visitados.pop(0)
        vertices_geral.remove(v)
        for adj in listaAdj[v]:
            if adj not in visitados and adj not in analizado:
                visitados.append(adj)
        analizado.append(v)
        
        if(len(visitados) == 0 and len(vertices_geral) != 0):
            visitados.append(vertices_geral[0])
            
    print(analizado) 
    return
   
    
BFS({0: [1, 3, 4], 
     1: [0, 2], 
     2: [1], 
     3: [0], 
     4: [0, 5], 
     5: [4],
     6: []}
    , 0)    



















#  visitados = []  # Lista para armazenar a sequência dos vértices visitados
#     fila = [v]  # Fila para a busca em largura, começando pelo vértice v
#     visitado = {v}  # Conjunto para marcar vértices já visitados

#     while fila:
#         vertice_atual = fila.pop(0)  # Remove o primeiro elemento da fila
#         visitados.append(vertice_atual)  # Marca o vértice como visitado

#         # Itera sobre os vizinhos do vértice atual
#         for vizinho in listaAdj[vertice_atual]:
#             if vizinho not in visitado:
#                 visitado.add(vizinho)  # Marca o vizinho como visitado
#                 fila.append(vizinho)  # Adiciona o vizinho à fila para ser processado

#     print(visitados) # Retorna a sequência dos vértices visitados