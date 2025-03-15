from random import randint
from time import sleep
vitorias = 0
while True:


    num = int(input("Digite um número para jogar com o computador(par ou impar): "))
    player = str(input("P/I: ")).upper()[0].strip()
    while player not in "PpIi":
        player = str(input("P/I: ")).upper()[0].strip()
    pc = randint(0,10)
    soma = pc + num
    sleep(0.5)
    print("Sou seu pc...escolhendo número...")
    sleep(1)
    print("Escolhi!!")
    print(f"Computador:{pc}\nJogador:{num}")
        
    if soma % 2 == 0 and player in "P":
        print("Parabens você venceu!Jogue novamente")
        print("~" * 40)
        vitorias += 1
    
    elif soma % 2 == 0 and player in "I":
        print(f"Você perdeu!Você tinha uma sequencia de {vitorias} vitorias")
        break

    elif soma % 2 == 1 and player in "P":
        print(f"Você perdeu!Você tinha uma sequencia de {vitorias} vitorias")
        break

    elif soma % 2 == 1 and player in "I":
        print("Você ganhou!Jogue novamente")
        print("~" * 40)
        vitorias += 1
