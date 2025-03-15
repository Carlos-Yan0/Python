num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: \n"))
menu = False

while menu == False:
    escolha = int(input("""    [1] soma
    [2] multiplicar
    [3] maior
    [4] novos números
    [5]sair do programa\n"""))
    
    if escolha == 1:
        resultado = num1 + num2
        print("A soma dos dois números é {}".format(resultado))
    
    elif escolha == 2:
        resultado = num1 * num2
        print("A multiplicação dos dois números é {}".format(resultado))

    elif escolha == 3:
        if num1 > num2:
            print("O maior número é {}".format(num1))
        elif num2 > num1:
            print("O maior número é {}".format(num2))
        else:
            print("Os dois números são iguais")

    elif escolha == 4:
        num1 = int(input("Digite outro número: "))
        num2 = int(input("Digite outro número: "))
    
    elif escolha == 5:
        menu = True

    else:
        print("Opção invalida!!")

print("Obrigado por usar nosso programa!!")
    