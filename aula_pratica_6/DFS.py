def DFS(graph, start, visited=None, result=None):
    # Inicializar 'visited' e 'result' apenas na primeira chamada da função
    first_call = visited is None and result is None
    if visited is None:
        visited = set()
    if result is None:
        result = []

    # Marcar o nó atual como visitado e adicioná-lo ao resultado
    visited.add(start)
    result.append(start)

    # Percorrer os vizinhos do nó atual
    for neighbor in graph.get(start, []):  # Utilizar .get() para evitar KeyError
        if neighbor not in visited:
            DFS(graph, neighbor, visited, result)

    # Imprimir apenas na chamada inicial (após a última recursão)
    if first_call:
        print(result)
    
    return result
