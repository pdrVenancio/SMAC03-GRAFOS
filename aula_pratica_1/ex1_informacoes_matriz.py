# Descrição: Retorna a dimensão da matriz no formato (linhas, colunas) e a lista com os valores da sua diagonal.
# Entrada: matriz de adjacências
# Saída: Dimensão da matriz (linhas, coluna), lista com valores da diagonal
import numpy as np
def dimensaoMatriz(matriz):
    diagonal = np.diagonal(matriz)
    print(np.shape(matriz), diagonal)
    
# Descrição: imprime o elemento da posição [i][j] informado pelo usuário. Informa caso algum índice dado como entrada seja
# maior que a dimensão da matriz.
# Entrada: matriz de adjacências
# Saída: Elemento da matriz na célula [i][j] ou mensagem de 'Erro'
def valorCelula(matriz ,i, j):
    linhas = len(matriz)
    colunas = len(matriz[0]) if linhas > 0 else 0
    
    if i > linhas or j > colunas:
        print('Erro')
        return
    
    print('Celula[{'+ str(i) +'}][{' + str(j) +'}]' + ': {'+ str(matriz[i][j]) + '}')
 
# Descrição: A partir da matriz, implemente uma função que constrói um dicionário. Cada chave do dicionário corresponde ao
# índice da linha da matriz. O valor de cada chave corresponde a uma lista com os índices das colunas associadas à linha em
# questão, que possuam valor maior que 0. Caso o valor da coluna seja maior que 1 deve-se repetir o índice da coluna conforme
# o valor (ex. a célula dada pela linha 1 e coluna 2 tem valor 4, logo, o valor 2 na lista da linha 1 precisará ser repetido 4 vezes).
# Entrada: matriz de adjacências
# Saída: representação da matriz como Dictionary.
def criaDicionario(matriz):    
    dic = {}
    for i, linha in enumerate(matriz):
        indices_colunas = []
        for j, valor in enumerate(linha):
            if valor > 0:
                indices_colunas.extend([j] * valor)
        dic[i] = indices_colunas
    print(dic)   
    
# Descrição: função que recebe um número x e imprime em cada linha um número correspondente a contagem regressiva de x
# até o valor 1. Utilize o comando “for”.
# Entrada: matriz de adjacências
# Saída: números inteiros
def contaRegressivaFor(n):
    for i in range(0, n):
        print(n - i)
        
# Descrição: função que recebe um número x e imprime em cada linha um número correspondente a contagem regressiva de x
# até o valor 1. Utilize o comando “while”.
# Entrada: matriz de adjacências
# Saída: números inteiros.
def contaRegressivaWhile(n):
    while(n > 0):
        print(n)
        n -= 1
    
# Descrição: função que recebe um número x e imprime em cada linha um número correspondente a contagem regressiva de x
# até o valor 1. Utilize uma estratégia de recursão.
# Entrada: matriz de adjacências
# Saída: números inteiros.
def contaRegressivaRecursao(n):
    if n < 1:
        return
    print(n)
    return contaRegressivaRecursao(n - 1)
    
matriz = []
arquivo = 'ponte.txt'
with open(arquivo, 'r') as file:
    for linha in file:
        matriz.append(list(map(int, linha.split())))

print('\n Dimensao da matriz e sua diagonal:\n')
dimensaoMatriz(matriz)

print('\n Retorna valor da celula:\n')
valorCelula(matriz ,1, 2)

print('\n Criação do dicionario:\n')
criaDicionario(matriz)

print('\n contagem regressiva FOR :\n')
contaRegressivaFor(10)

print('\n contagem regressiva WHILE :\n')
contaRegressivaWhile(10)

print('\n contagem regressiva recursao :\n')
contaRegressivaRecursao(10)
