from math import radians, cos, tan, sin

Angulo = int(input("Digite um angulo para descobrir a tangente, o cosseno e o seno: "))

tan = tan(radians(Angulo))
cos = cos(radians(Angulo))
seno = sin(radians(Angulo))

print("O angulo de {} Graus tem uma tangente de valor:{:.2f}\n Cosseno:{:.2f}\n seno:{:.2f}".format(Angulo, tan, cos, seno))