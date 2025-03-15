lista = list()
while True:
    num = int(input("Digite um número: "))
    if num not in lista:
        print("Valor adicionado com sucesso! ")
        lista.append(num)
    else:
        print("Valor duplicado, não vou adicionar ele...")

    conti = str(input("Deseja continuar[S/N]: ")).strip().upper()[0]
    while conti not in "NS":
        conti = str(input("Deseja continuar[S/N]: ")).strip().upper()[0]

    if conti in "N":
        break
    elif conti in "S":
        print("Número registrado...")
        
lista.sort()
print(f"Os valores digitados foram {lista}")