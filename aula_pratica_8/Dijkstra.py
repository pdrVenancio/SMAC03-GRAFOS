# Vértice Aberto e Fechado: Normalmente, considera-se que um vértice 
# v é "aberto" se ele não possui todas as conexões (arestas) que poderia 
# ter com outros vértices no grafo. Ou seja, ele não tem todas as arestas
# possíveis conectadas a ele. Por outro lado, um vértice é "fechado" 
# quando possui todas as arestas possíveis conectadas a ele (no caso de 
# um grafo completo, por exemplo, todos os vértices seriam "fechados").


def dijkstra(grafo):
    custo = [ -1  for i in range(len(grafo))]
    rota = [0 for i in range(len(grafo))]
    custo[0] = 0
    
    vertices_abertos = [vertice for vertice in range(len(grafo)) if 0 in grafo[vertice]]
    vertices_fechados = [vertice for vertice in range(len(grafo)) if 0 not in grafo[vertice]]
    
    while len(vertices_abertos) != 0:
        # vertice com menor custo
        v = vertices_abertos[0] 
        menor_custo = custo[v]  
        for vertice in vertices_abertos:
            if custo[vertice] != -1 and custo[vertice] < menor_custo:
                menor_custo = custo[vertice]
                v = vertice
        
        vertices_fechados.append(v)
        vertices_abertos.remove(v)
        

        for u in range(len(grafo)):
            if grafo[v][u] > 0:  # Existe uma aresta de v para u
                if custo[u] == -1 or custo[v] + grafo[v][u] < custo[u]:
                    custo[u] = custo[v] + grafo[v][u]
                    rota[u] = v
    
    print(custo)
    print(rota)
    return    
     
        
matriz_adjacencia = [
    [0, 3, 8, 4, 0, 10],  
    [3, 0, 0, 6, 0, 0],   
    [8, 0, 0, 0, 7, 0],   
    [4, 6, 0, 0, 1, 3],   
    [0, 0, 7, 1, 0, 1],  
    [10, 0, 0, 3, 1, 0]   
]       
dijkstra(matriz_adjacencia)
    
    

    
    
    

        