num = int(input("Digite um número para converter: "))

#variavel

escolha = int(input("Conversor de numeros\n1. Binario\n2. Octal\n3. Hexadecimal\n"))

#mostra na tela as escolhas

if escolha == 1:
    num_convertido = bin(num)
    print("O número {} convertido para Binario é {}".format(num, num_convertido[2:]))

elif escolha == 2:
    num_convertido = oct(num)
    print("O número {} convertido para Octal é {}".format(num, num_convertido[2:]))

elif escolha == 3:
    num_convertido = hex(num)
    print("O número {} convertido para Hexadecimal é {}".format(num, num_convertido[2:]))

else:
    print("Opção invalida")
