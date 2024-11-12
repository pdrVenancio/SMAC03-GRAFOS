def prim(grafo):
    vertice = 0
    JA_selecionados = []
    JA_selecionados.append(vertice)
    NAO_selecionados = [i for i in range(len(grafo))]
    NAO_selecionados.remove(vertice)
    arestas_AGM = []
    custo = 0

    while len(arestas_AGM) < (len(grafo) - 1):
        menor = None
        u = None
        par_aresta = None
        for selecionada in JA_selecionados:
            for nao_selecionada in NAO_selecionados:
                if menor == None and grafo[selecionada][nao_selecionada] != 0:
                    menor = grafo[selecionada][nao_selecionada] 
                    u = nao_selecionada
                    par_aresta = [selecionada, nao_selecionada]
                    
                elif menor != None and grafo[selecionada][nao_selecionada] < menor and grafo[selecionada][nao_selecionada] != 0:    
                    menor = grafo[selecionada][nao_selecionada]
                    u = nao_selecionada
                    par_aresta = [selecionada, nao_selecionada]
                else:
                    pass

        custo += menor 
        JA_selecionados.append(u)
        NAO_selecionados.remove(u)
        arestas_AGM.append(par_aresta)

    return arestas_AGM, custo


grafo = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]

print(prim(grafo))