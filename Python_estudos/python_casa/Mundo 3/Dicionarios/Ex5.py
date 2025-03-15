dados = list()
pessoas = dict()
media = 0
while True:
    pessoas["nome"] = str(input("Nome: "))
    pessoas["idade"] = int(input("Idade: "))
    media += pessoas["idade"]
    pessoas["sexo"] = str(input("Sexo(M/F): ")).upper().strip()[0]

    while pessoas["sexo"] not in "MF":
        print("ERRO, TENTE NOVAMENTE!!")
        pessoas["sexo"] = str(input("Sexo(M/F): ")).upper().strip()[0]
    cont = str(input("Deseja continuar(S/N): ")).strip().upper()[0]

    dados.append(pessoas.copy())
    pessoas.clear()

    while cont not in "SN":
        print("ERRO, TENTE NOVAMENTE!!")
        cont = str(input("Deseja continuar(S/N): ")).strip().upper()[0]
    if cont in "N":
        break

print(dados)
print(f"O número de pessoas cadastradas é de {len(dados)}")
media = media / len(dados)
print(f"A média de idade é {media:.2f}")
print(f"As mulheres cadastradas foram ", end = "")
for p in dados:
    if p["sexo"] in "F":
        print(f"{p["nome"]}", end = " ")

print()

print("Lista das pessoas acima da média(idade)")
for p in dados:
    print("       ", end = "")
    if p["idade"] >= media:
        for k, v in p.items():
            print(f"{k} = {v}", end = " ")
        print()