sexo = str(input("Digite o seu sexo[F/M]: ")).upper()[0].strip()
if sexo not in "MF":
    print("Invalido, tente novamente!")

while sexo not in "MF":
    sexo = str(input("Digite o seu sexo[F/M]: ")).upper()[0].strip()
    if sexo not in "MF":
        print("invalido, tente novamente!")