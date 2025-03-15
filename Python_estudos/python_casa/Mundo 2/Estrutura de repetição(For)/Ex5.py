soma = 0
for c in range(1, 7):
    num = int(input("Digite um numero: "))
    if num % 2 == 0:
        soma += num
print("A soma dos número pares é {}".format(soma))