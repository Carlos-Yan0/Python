dados = list()
pessoas = list()
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        menorp = maiorp = dados[1]
    else:
        if maiorp < dados[1]:
            maiorp = dados[1]
        elif menorp > dados[1]:
            menorp = dados[1]
    pessoas.append(dados[:])
    dados.clear()

    conti = str(input("Deseja continuar[S/N]: ")).strip().upper()[0]
    if conti in "N":
        break

print(f"Foram cadastradas {len(pessoas)} pessoas")
print(f"O menor peso foi {menorp} das pessoas:", end = "")
for p in pessoas:
    if p[1] == menorp:
        print(f"[{p[0]}]", end = " ")
print()
print(f"O maior peso foi {maiorp} das pessoas:", end = "")
for p in pessoas:
    if p[1] == maiorp:
        print(f"[{p[0]}]", end = " ")