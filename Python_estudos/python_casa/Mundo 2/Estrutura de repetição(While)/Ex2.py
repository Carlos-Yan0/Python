from random import randint

pc = randint(0, 10)
tenta = 0
acertou = False

while acertou == False:

    player = int(input("Digite um número de 0 a 10: "))
    tenta += 1

    if pc == player:
        acertou = True
    
    else:
        if pc > player:
            print("Mais!! tente de novo: ")
        elif player > pc:
            print("Menoss!!Tente de novo: ")

    

print("Parabens, você precisou de {} tentativas!".format(tenta))