numeros = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco",
            "Seis", "Sete", "Oito", "Nove", "Dez",
              "Onze", "Doze", "Treze", "Quatorze", "Quinze",
                "Dezesseis", "Dezesete", "Dezoito", "Dezenove", "Vinte")

while True:
    num = int(input("Digite um número de 0  a 20: "))
    if 0 <= num <= 20:
        print(f"O número {num} por extenso é {numeros[num]}")
        cont = str(input("Deseja continuar[S/N]: ")).strip().upper()[0]
        if cont in "N":
            break

    else:
        print("Digite um valor Valido! ")

print("Obrigado por usar nosso programa!! ")
    