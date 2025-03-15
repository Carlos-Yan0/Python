lista = list()
while True:
    num = int(input("Digite um número: "))
    lista.append(num)

    conti = str(input("Deseja continuar[S/N]: ")).strip().upper()[0]
    if conti in "N":
        break

    elif conti not in "S":
        print("Tente novamente!")
        while True:
            conti = str(input("Deseja continuar[S/N]: ")).strip().upper()[0]
            if conti in "SN":
                break
            else:
                print("Tente novamente!")
        if conti in "N":
            break

lista.sort(reverse = True)
print(f"Tivemos {len(lista)} números nessa lista!")
print(f"A lista em ordem decrescente fica: {lista}")
if 5 in lista:
    print("Na lista tem o número 5!")
else:
    print("A lista não contem o número 5")