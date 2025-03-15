def lenumeroint():
    num = input("Digit eum número inteiro: ")
    return int(num)

def soma(num1, num2):
    resultado = num1 + num2
    return resultado

n1 = lenumeroint()
n2 = lenumeroint()
res = soma(n1, n2)
print(f"A soma é {res}")