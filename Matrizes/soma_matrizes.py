def soma_Matriz(mat1, mat2):
    tam = len(mat1)
    mat_soma = [[0 for j in range(tam)] for i in range(tam)]
    for i in range(tam):
        for j in range(tam):
            mat_soma[i][j] = mat1[i][j] + mat2[i][j]
    return mat_soma

def multiMatriz(mat1, mat2):
    tam = len(mat1)
    matMulti = [[0 for j in range(tam)] for i in range(tam)]
    for i in range(tam):
        for j in range(tam):
            matMulti[i][j] = mat1[i][j] * mat2[i][j]
    return matMulti


def imprimeMatriz(mat):
    for linha in mat:
        for numero in linha:
            print(numero, end = " ")
        print()

def leMatriz(dimensao):
    mat = [[] for i in range(dimensao)]
    for i in range(dimensao):
        for j in range(dimensao):
            num = int(input("("+str(i+1)+","+str(j+1)+"): "))
            mat[i].append(num)
    return mat



n = int(input("Dimensão das matrizes: "))
mat1 = leMatriz(n)
mat2 = leMatriz(n)
print("mat1: ")
imprimeMatriz(mat1)
print("mat2: ")
imprimeMatriz(mat2)
mat3 = soma_Matriz(mat1, mat2)
print("soma: ")
imprimeMatriz(mat3)
mat3mult = multiMatriz(mat1, mat2)
print("multiplicação: ")
imprimeMatriz(mat3mult)
