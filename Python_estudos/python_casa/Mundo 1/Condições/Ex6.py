num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite o ultimo número: "))
menor = num1

if num2 < num1 and num2 < num3:
    menor = num2

elif num3 < num1 and num3 < num2:
    menor = num3

maior = num1

if num2 > num1 and num2 > num3:
    maior = num2

elif num3 > num1 and num3 > num2:
    maior = num3

print("O menor número é {} e o maior é {}".format(menor, maior))
