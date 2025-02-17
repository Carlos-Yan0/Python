def potencia(a, b):
    res = 1
    for c in range(b):
        res *= a
    return res



num1 = int(input("Digite um número: "))
num2 = int(input("Digite a quantidade de vezes que deseja elevar o primeiro número: "))

print(f"{num1} elevado a {num2} é {potencia(num1, num2)}")