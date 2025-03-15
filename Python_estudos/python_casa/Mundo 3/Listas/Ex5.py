completa = list()
while True:
    completa.append(int(input("Digite um número: ")))
    while True:
        conti = str(input("Deseja continuar[S/N]: ")).strip().upper()[0]
        if conti in "SN":
            break
        elif conti not in "SN":
            print("Tente novamente")
    if conti in "N":
        break

pares = list()
impares = list()

for c, v in enumerate(completa):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print(f"A lista completa é: {completa}")
print(f"Os números pares da lista são: {pares}")
print(f"Os números impares da lista são: {impares}")

    

    