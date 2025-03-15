from random import randint
player = int(input("Digite [0] para pedra, [1] para papel e [2] para tesoura: "))
pc = randint(0, 2)
match player:
    case 0:
        if pc == 0:
            print("Empate!")
        elif pc == 1:
            print("Perdeu!")
        elif pc == 2:
            print("Ganhou!")
    case 1:
        if pc == 0:
            print("Ganhou!")
        elif pc == 1:
            print("Empate!")
        elif pc == 2:
            print("Perdeu!")
    case 2:
        if pc == 0:
            print("Perdeu!")
        elif pc == 1:
            print("Ganhou!")
        elif pc == 2:
            print("Empate!")