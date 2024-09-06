# verificaAdjacencia(matriz, vi, vj)
# Descrição: Verifica se os vértices vi e vj são adjacentes.
# Entrada: matriz de adjacências, vi e vj (ambos números inteiros que indica o id do vértice)
# Saída: Boolean (True se os vértices são adjacentes; False caso contrário) 

def verificaAdjacencia(matriz, vi, vj):
    if(matriz[vi][vj] == 1 and matriz[vj][vi] ==1):
        print(True)
        return
    print(False)
