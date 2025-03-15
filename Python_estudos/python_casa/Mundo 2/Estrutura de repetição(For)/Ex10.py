for c in range(1, 6):
    peso = float(input("Digite um peso(em kg): "))

    if c == 1:
        maior = peso
        menor = peso

    elif peso > maior:
        maior = peso

    elif peso < menor:
        menor = peso

print("o maior peso é {} e o menor é {}".format(maior, menor))