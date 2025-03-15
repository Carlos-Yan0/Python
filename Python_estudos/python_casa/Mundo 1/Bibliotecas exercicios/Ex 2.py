import math

CO = float(input("Digite o comprimento do cateto oposto(em Cm): "))
CA = float(input("Digite o comprimento do cateto adjacente(em Cm): "))

HP = math.hypot(CO, CA)
print("O cateto oposto tem {} Cm de comprimento, o cateto adjacente tem {} Cm de comprimento e a hipotenusa tem {:.2f} Cm de comprimento ".format(CO, CA, HP))