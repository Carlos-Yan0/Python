def area(a, b):
    print(f"A área do terreno é {a*b}")
    

print("-" * 20)
print("Medidor de Terrenos")
print("-" * 20)
l = float(input("Digite a largura do terreno: "))
c = float(input("Digite o comprimento do terreno: "))
area(l, c)