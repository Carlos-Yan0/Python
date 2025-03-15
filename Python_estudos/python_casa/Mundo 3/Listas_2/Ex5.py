from random import randint
quant = int(input("Digite quantos jogos deseja jogar: "))
jogos = list()
t_jogos = list()
tot = 0
while tot < quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogos:
            jogos.append(num)
            cont += 1
        if cont >= 6:
            break
    t_jogos.append(jogos[:])
    jogos.clear()
    tot += 1

for i, j in enumerate(t_jogos):
    print(f"{i+1} jogo:{j}")
