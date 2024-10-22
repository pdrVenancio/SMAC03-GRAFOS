
def coloracaoSequencial(grafo,vertice):
    id_cor = 0
    cor = [0 for _ in range(len(grafo))]

    for adjacente in grafo[vertice]:
        print(adjacente)
        if id_cor not in adjacente:
            cor[vertice] = id_cor
        else:
            id_cor += 1
            cor[vertice] = id_cor
    
    return cor



grafo = {
    0: [1, 3],  
    1: [4],  
    2: [4, 5], 
    3: [1],    
    4: [3],
    5: [5]
}
print(coloracaoSequencial(grafo, 5))