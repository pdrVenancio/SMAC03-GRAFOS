def tempoVertice(grafo, v):
    cor = ['branco' for _ in range(len(grafo))]
    tempoD = [0 for _ in range(len(grafo))]
    tempoT = [0 for _ in range(len(grafo))]
    tipo_aresta = {} 
    tempo = [0] 
    
    lista_tempo = {}
    
    visitaDFS(grafo, v, cor, tipo_aresta, tempoD, tempoT, tempo)
    
    for vertice in grafo:
        if cor[vertice] == 'branco':
            visitaDFS(grafo, vertice, cor, tipo_aresta, tempoD, tempoT, tempo)
        lista_tempo[vertice] = str(tempoD[vertice]) +  '/' + str(tempoT[vertice])
    
    return lista_tempo


def visitaDFS(grafo, vertice, cor, tipo_aresta, tempoD, tempoT, tempo):
    cor[vertice] = 'cinza'
    tempo[0] += 1
    tempoD[vertice] = tempo[0]

    for adjacente in grafo[vertice]:
        if cor[adjacente] == 'branco':
            visitaDFS(grafo, adjacente, cor, tipo_aresta, tempoD, tempoT, tempo)
    
    cor[vertice] = 'preto'
    tempo[0] += 1
    tempoT[vertice] = tempo[0]

# exemplo slide
grafo = {
    0: [1, 3],  
    1: [4],  
    2: [4, 5], 
    3: [1],    
    4: [3],
    5: [5]
}

print(tempoVertice(grafo, 5))

