from datetime import date

soma = 0
ano_atual = date.today().year

for c in range(0, 7):
    nasc = int(input("Digite a data de nascimento: "))
    if (ano_atual - nasc) >= 21:
        soma += 1

print("A quantidade de pessoas maior de idade é {} e tem {} pessoas menores de idade".format(soma, 7 - soma))