# calcDensidade(matriz)
# Descrição: Retorna o valor da densidade do grafo.
# Entrada: matriz de adjacências
# Saída: Float (valor da densidade com precisão de três casas decimais) 

def calcDensidade(matriz):
    simples = True
    # verifico normal: simetrico
    # dirigido: nao simetrico
    for i,linha in enumerate(matriz):
        for j, valor in enumerate(linha):
            if matriz[i][j] != matriz[j][i]:
                    simples = False
    
    e = 0
    v = 0 
    
    for i,linha in enumerate(matriz):
        for j, valor in enumerate(linha):
            if matriz[i][j] == 1 and matriz[j][i] == 1:
                e += 1
    v = len(matriz[0])            
    
    if simples:    
        densidade = (2 * e) / (v * (v-1))
    else:
        densidade =  e / (v * (v-1))
          
    
    
    print(round(densidade,3))
    return

matriz  =[[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]]
calcDensidade(matriz)