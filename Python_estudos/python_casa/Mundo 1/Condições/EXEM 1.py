n1 = float(input("Digite uma nota: "))
n2 = float(input("Digite outra nota: "))
m = (n1 + n2) / 2
print("Sua média foi de {:.1f}".format(m))
if m<5:
    print("Nota insuficiente, você foi reprovado!")

elif m<=6:
    print("você ficou de recuperação!")

else:
    print("Parabens, você foi aprovado!")