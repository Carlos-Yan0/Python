lista = list()
for c in range(0, 5):
    lista.append(int(input(f"Digite um número para a posição {c}: ")))
    if c == 0:
       menor = maior = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if menor > lista[c]:
            menor = lista[c]

print(f"A lista completa é:{lista}")
print(f"O maior número é {maior} e aparece nas posições: ", end = "")
for c, v in enumerate(lista):
    if v == maior:
        print(f"{c}..", end = "")

print(f"\nO menor número é {menor} e aparece nas posições: ", end = "")
for c, v in enumerate(lista):
    if v == menor:
        print(f"{c}..", end = "")

