class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find_set(self, x):
        # FIND-SET com compressão de caminhos
        if self.parent[x] != x:
            self.parent[x] = self.find_set(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find_set(x)
        rootY = self.find_set(y)
        if rootX != rootY:
            # União por rank para otimizar a altura da árvore
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def kruskcal(grafo):    
    peso_total = 0
    arestas_ordenadas = []
    n = len(grafo)
    uf = UnionFind(n)

    for i in range(n):
        for j in range(i + 1, n): # pega o triangulo superior da matriz
            if grafo[i][j] != 0:
                arestas_ordenadas.append([grafo[i][j],i,j])
    
    arestas_ordenadas.sort()    

    arestas_AGM = []
    while len(arestas_AGM) < len(grafo) - 1:
        for peso, u, v in arestas_ordenadas:
            if uf.find_set(u) != uf.find_set(v):
                uf.union(u, v)
                arestas_AGM.append((u, v))
                peso_total += peso
                
    return arestas_AGM, peso_total

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

print(kruskcal(grafo))