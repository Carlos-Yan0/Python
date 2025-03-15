num = int(input("Digite um número para ver sua tabuada de 1 a 10: "))
for num2 in range(1, 11):
    print("{}X{}={}".format(num, num2, num * num2))