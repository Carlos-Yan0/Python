matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sp = sc = m2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valora para [{l}, {c}]: "))
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end = "")
        if matriz[l][c] % 2 == 0:
            sp += matriz[l][c]         
    print()

print(f"A soma de todos os números pares é: {sp}")
for l in range(0, 3):
    sc += matriz[l][2]
print(f"A soma de todos os números da terceira coluna é: {sc}")
for c in range(0, 3):
    if m2 < matriz[1][c]:
        m2 = matriz[1][c]
print(f"O maior número da linha 2 é: {m2}")