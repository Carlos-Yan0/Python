#criação da lista notas e variavel soma
notas = list()
soma = 0

#variavel que indica quantidade de notas
q_notas = int(input("Quantas notas deseja adicionar: "))

for n in range(q_notas):#for para adicionar as notas a lista
    notas.append(float(input(f"Digite a nota {n + 1}: "))) #add notas a lista
    soma += notas[n]#adiciona as notas a variavel soma

media = soma / len(notas) #tira a media

#print das notas e da media
print(notas)
print(f"{media:.2f}")
