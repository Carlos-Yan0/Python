nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media < 5:
    print("Você foi reprovado!\nmedia:{:.1f}".format(media))

elif media <= 6.9:
    print("Você esta de recuperação!\nmedia:{:.1f}".format(media))

else:
    print("Você foi aprovado!\nmedia:{:.1f}".format(media))