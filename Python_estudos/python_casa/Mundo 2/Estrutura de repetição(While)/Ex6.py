termo1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao da progressao aritmetica: "))
continuar = True
quantidade = 0



while continuar == True:
    termos = termo1 + razao
    escolha = int(input("""\n    Escolha o que deseja!!
    [1]mostrar os 10 primeiros termos
    [2]escolher a quantidade de termos
    [3]parar o programa\n"""))
    
    if escolha == 1:
        c = 10
        quantidade += 10
        print("{}".format(termo1), end = " ")
        while c > 1:
            print("{}".format(termos), end = " ")
            termos += razao
            c -= 1
            
    
    elif escolha == 2:
        c = int(input("Digite a quantidade de termos que deseja saber: "))
        quantidade += c
        print("{}".format(termo1), end = " ")
        while c > 1:
            print("{}".format(termos), end = " ")
            termos += razao
            c -= 1
    elif escolha == 3:
        continuar = False
print("Obrigado por usar nosso programa!\n ao todo foram {} termos".format(quantidade))
            
            
        
