def ordenacaoTopologicaKahn(grafo):
    lista_elementos = []
    grau_entrada = {i: 0 for i in range(len(grafo))} 

    # Calcula o grau de entrada de cada vértice
    for ver in grafo:
        for adj in grafo[ver]:
            grau_entrada[adj] += 1

    # listo todos os vertices sem grau de entrada
    sem_grau_entrada = [vertice for vertice in grafo if grau_entrada[vertice] == 0]

    while sem_grau_entrada:
        vertice_atual = sem_grau_entrada.pop()  
        lista_elementos.append(vertice_atual)

        for adj in grafo[vertice_atual]:
            grau_entrada[adj] -= 1
            if grau_entrada[adj] == 0:
                sem_grau_entrada.append(adj)

    if len(lista_elementos) != len(grafo):
        return 'Não é um DAG!'
    
    return lista_elementos


grafo = {0: [1], 1: [], 2: [0], 3: [1, 2], 4: [1, 2]}
print(ordenacaoTopologicaKahn(grafo))
