def leMatriz(dimensao):
    mat = [[] for i in range(dimensao)]
    for i in range(dimensao):
        for j in range(dimensao):
            num = int(input("("+str(i+1)+","+str(j+1)+"): "))
            mat[i].append(num)
    return mat

print(leMatriz(3))