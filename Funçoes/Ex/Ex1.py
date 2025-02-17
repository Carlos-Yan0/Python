def verificarNum(a):
    if a > 0:
        return "Positivo"
    elif a == 0:
        return "Zero"
    else:
        return "Negativo"
    
num = int(input("Digite um número: "))

print(f"Seu número é {num} e ele é {verificarNum(num)}")