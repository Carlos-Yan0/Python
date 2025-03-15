termo_1 = int(input("Digite o primeiro termo da progressao: "))
razao = int(input("Digite a razão da progressao: "))
c = 10
print("{}".format(termo_1), end = " ")
soma = termo_1 + razao

while c > 1:
    print(soma, end = " ")
    soma += razao
    c -= 1