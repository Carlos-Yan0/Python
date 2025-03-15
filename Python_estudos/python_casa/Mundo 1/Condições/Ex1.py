import random

#lista = [0, 1, 2, 3, 4, 5]
#num = random.choice(lista)
#res = int(input("Digite um número de 0 a 5: "))
#if res == num:
 #   print("Parabens você ganhou!")
#else:
 #   print("Você perdeu!")

num = random.randint(0, 5)
tentativa = int(input("Digite um número entre 0  e 5: "))

if tentativa == num:
    print("Você ganhou!!")

else:
    print("Você perdeu! O número era {}".format(num))
