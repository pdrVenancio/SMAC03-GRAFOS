def  removeAresta(matriz, vi, vj):
    if matriz[vi][vj] > 0: 
        matriz[vi][vj] -= 1  
    if matriz[vj][vi] > 0:
        matriz[vj][vi] -= 1   
    print(matriz)
