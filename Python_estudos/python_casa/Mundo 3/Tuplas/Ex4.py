num = (int(input("Digite um número: ")),
        int(input("Digite um número: ")),
        int(input("Digite um número: ")),
        int(input("Digite um número: ")))

pares = 0
for c in num:
    if c % 2 == 0:
        pares += 1

print(f"O valor 9 apareceu {num.count(9)} vez(es)")
if 3 in num:
    print(f"O valor 3 apareceu na posição {num.index(3) + 1}")
else:
    print("O valor 3 não esta entre os digitados")
print(f"A quantidade de números pares é {pares}")
