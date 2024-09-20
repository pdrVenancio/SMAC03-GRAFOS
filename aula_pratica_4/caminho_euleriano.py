def caminhoEuleriano(matriz):
    n = len(matriz)
    total = 0 
    i = 0
    while total <= 2 and i < n:
        grau = sum(1 for j in matriz[i] if j == 1)
        if grau % 2 != 0:
            total = total + 1
        i += 1
    
    if total > 2:
        print(False) 
    else:
        print(True)

caminhoEuleriano([[0, 2, 2, 1], 
                  [2, 0, 0, 1], 
                  [2, 0, 0, 1], 
                  [1, 1, 1, 0]
                ])