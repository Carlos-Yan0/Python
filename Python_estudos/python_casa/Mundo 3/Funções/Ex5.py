def sortear(a):
    for c in range(0, 5):
        a.append(randint(0, 10))
    print("Sorteando 5 números....")
    sleep(1)
    print(f"Os números sorteados foram {a}")

def somapar(lista):
    s = 0
    for valor in lista:
        if valor % 2 == 0:
            s += valor
    print(f"A soma de todos os números páres sorteados é {s}")


from random import randint
from time import sleep
sorteio = list()
sortear(sorteio)
somapar(sorteio)
