from random import choice, randint

#lista = ["Pedra", "Papel", "Tesoura"]
#pc = choice(lista)

lista = ("Pedra", "Papel", "Tesoura")
pc = randint(0, 2)
pc = lista[pc]

player = int(input("Escolha um para jogar contra a maquina\n1. Pedra\n2. Papel\n3. Tesoura\n"))

if player == 1:
    player = "Pedra"
    
    if player == pc:
        print("Empate\n pc:{}\nplayer:{}".format(pc, player))
    
    elif pc == "Papel":
        print("Você perdeu!\npc:{}\nplayer:{}".format(pc, player))

    elif pc == "Tesoura":
        print("Você ganhou!!\npc:{}\nplayer:{}".format(pc, player))

elif player == 2:
    player = "Papel"

    if player == pc:
        print("Empate\n pc:{}\nplayer:{}".format(pc, player))
    
    elif pc == "Pedra":
        print("Você ganhou!!\n pc:{}\nplayer:{}".format(pc, player))

    elif pc == "Tesoura":
        print("Você perdeu!!\n pc:{}\nplayer:{}".format(pc, player))

elif player == 3:
    player = "Tesoura"

    if player == pc:
        print("Empate\n pc:{}\nplayer:{}".format(pc, player))

    elif pc == "Papel":
        print("Você ganhou!!\n pc:{}\nplayer:{}".format(pc, player))

    elif pc == "Pedra":
        print("Você perdeu!!\n pc:{}\nplayer:{}".format(pc, player))
