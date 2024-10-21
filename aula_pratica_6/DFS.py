def DFS(graph, start):
    def dfs_recursive(graph, start, visited=None, result=None):
        if visited is None:
            visited = set()  # Conjunto de vértices visitados
        if result is None:
            result = []  # Lista para armazenar a sequência dos vértices visitados

        visited.add(start)
        result.append(start)

        for neighbor in graph[start]:
            if neighbor not in visited:
                dfs_recursive(graph, neighbor, visited, result)

        return result

    result = dfs_recursive(graph, start)
    print(result)