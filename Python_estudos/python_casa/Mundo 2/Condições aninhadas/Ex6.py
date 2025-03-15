from datetime import date

nascimento = int(input("Digite a data de nascimento: "))
idade = date.today().year - nascimento

if nascimento > date.today().year:
    print("OLOCO UM VIAJANTE DO TEMPO")

elif idade <= 9:
    print("Mirim")

elif idade <= 14:
    print("Infantil")

elif idade <= 19:
    print("Junior")

elif idade <= 25:
    print("Senior")

elif idade > 25:
    print("Master")
