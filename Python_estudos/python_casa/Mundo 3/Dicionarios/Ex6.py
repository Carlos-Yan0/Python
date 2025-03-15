galera = list()
jogadores = dict()
gols = list()

while True:
    jogadores["nome"] = str(input("Digite o nome do jogador: "))
    tot_partidas = int(input(f"Quantas partidas {jogadores["nome"]} jogou: "))
    for c in range(0, tot_partidas):
        gols.append(int(input(f"Quantos gols na partida {c + 1}: ")))
    tot_gols = sum(gols)
    jogadores["tot_gols"] = tot_gols
    jogadores["gols"] = gols[:]
    galera.append(jogadores.copy())
    gols.clear()
    jogadores.clear()
    tot_gols = 0

    cont = str(input("Deseja continuar(S/N): ")).strip().upper()[0]
    while cont not in "SN":
        print("Erro, opção invalida!")
        cont = str(input("Deseja continuar(S/N): ")).strip().upper()[0]
    if cont == "N":
        break


print("cod  ", end = "")
for k in galera[0].keys():
    print(f"{k:<15}", end = "")
print()
print("-" * 50)
print()
for c, v in enumerate(galera):
    print(f"{c:>2}  ", end = " ")
    for j in v.values():
        print(f"{str(j):<15}", end = "")
    print()
print("-" * 50)
escolha = 0
while escolha != 999:
    escolha = int(input("Digite o codigo do jogador para ver mais(999 para parar): "))
    if escolha == 999:
        break
    else:
        if len(galera) <= escolha:
            escolha = int(input("Digite o codigo do jogador para ver mais(999 para parar): "))
        else:
            print(f"Levantamento do jogador {galera[escolha]["nome"]}")
            for p, g in enumerate(galera[escolha]["gols"]):
                print(f"Na partida {p + 1}, fez {g} gols")
            print("-" * 50)
print("Volte sempre")
