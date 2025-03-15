from random import randint
from operator import itemgetter
from time import sleep
jogo = {"jogador1": randint(1,6),
        "jogador2": randint(1,6),
        "jogador3": randint(1,6),
        "jogador4": randint(1,6)}
for k, v in jogo.items():
    print(f"{k} sorteou {v}")
    sleep(0.6)
ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse = True )
print("-=" * 30)
for r, j in enumerate(ranking):
    print(f"{r + 1} lugar - {j[0]} com {j[1]} pontos")
    sleep(0.5)