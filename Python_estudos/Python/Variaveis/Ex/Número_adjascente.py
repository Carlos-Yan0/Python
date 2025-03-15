lista = []
num = int(input("Digite a quantidade de números que deseja verificar: "))

for c in range(num):
    n = int(input("Digite um número: "))
    lista.append(n)

adjascente = False


for i in range(len(lista) - 1):
    if lista[i] == lista[i + 1]:
        adjascente = True
        break


print(f"para n = {lista}, a resposta é {'sim' if adjascente else 'não'}")
