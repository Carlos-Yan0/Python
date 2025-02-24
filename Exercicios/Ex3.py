#criação das duas listas e variavel contadora
num1 = list()
num2 = list()
cont = 0

#add valores a primeira lista
for c in range(5):
    num1.append(int(input(f"Digite o valor {c + 1} da primeira lista: ")))

#add valores a segunda lista
for c in range(5):
    num2.append(int(input(f"Digite o valor {c + 1} da segunda lista: ")))

#os dois for servem para verificar os numeros da lista, sem fazer distinção de posição
for n in range(5):
    for n2 in range(5):
        if num1[n] == num2[n2]:
            print(num1[n], end = " ")
            cont += 1

#usamos o cont para verficar uma lista sem repetições
if cont == 0:
    print("Não tem número repetidos")
    