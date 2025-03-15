num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 < num2:
    print("O primeiro valor ({}) é menor que o segundo valor ({})".format(num1, num2))

elif num2 < num1:
    print("O primeiro valor ({}) é maior que o segundo valor ({})".format(num1, num2))

elif num1 == num2:
    print("O primeiro valor ({}) é igual ao segundo valor ({})".format(num1, num2))