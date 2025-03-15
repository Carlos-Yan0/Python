dados = dict()
gols = list()
dados["nome"] = str(input("Digite o nome do jogador: "))
tot = int(input(f"Quantas partidas {dados["nome"]} jogou: "))
for c in range(0, tot):
    gols.append(int(input(f"Quantos gols na partida {c}: ")))
dados["gols"] = gols[:]
quant_gols = sum(gols)
print("-=" * 15)
print(f"nome:{dados["nome"]}")
for k, v in enumerate(dados["gols"]):
    print(f"Na partida {k} o jogador {dados["nome"]} fez {v} gols")
print(f"Em {tot} partidas o jogador fez {quant_gols} gols")