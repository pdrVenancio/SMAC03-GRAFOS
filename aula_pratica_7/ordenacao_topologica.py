def classificaArestaDFS(grafo):
    cor = ['branco' for _ in range(len(grafo))]
    tempoD = [0 for _ in range(len(grafo))]
    tempoT = [0 for _ in range(len(grafo))]
    lista_elementos = []
    tipo_aresta = {} 
    tempo = [0] 
    
    for vertice in grafo:
        if cor[vertice] == 'branco':
            visitaDFS(grafo, vertice, cor, tipo_aresta, tempoD, tempoT, tempo, lista_elementos)
    
    print(f'Cor: {cor}\nTipo de aresta: {tipo_aresta}\nTempoD: {tempoD}\nTempoT: {tempoT}\n Ordenação topologica: {lista_elementos}')


def visitaDFS(grafo, vertice, cor, tipo_aresta, tempoD, tempoT, tempo, lista_elementos):
    cor[vertice] = 'cinza'
    tempo[0] += 1
    tempoD[vertice] = tempo[0]

    for adjacente in grafo[vertice]:
        if cor[adjacente] == 'branco':
            tipo_aresta[(vertice, adjacente)] = 'tree'
            visitaDFS(grafo, adjacente, cor, tipo_aresta, tempoD, tempoT, tempo, lista_elementos)
        elif cor[adjacente] == 'cinza':
            tipo_aresta[(vertice, adjacente)] = 'back'
        else:
            if tempoD[vertice] < tempoD[adjacente]:
                tipo_aresta[(vertice, adjacente)] = 'forward'
            else:
                tipo_aresta[(vertice, adjacente)] = 'cross'
    
    cor[vertice] = 'preto'
    tempo[0] += 1
    tempoT[vertice] = tempo[0]
    lista_elementos.insert(0, vertice)

# exemplo slide
grafo = {
    0: [1, 3],  
    1: [4],  
    2: [4, 5], 
    3: [1],    
    4: [3],
    5: [5]
}
classificaArestaDFS(grafo)

