parar = False
contagem = soma = 0

while parar == False:
    num = int(input("Digite um número(999 para parar): "))
    
    if num != 999:
        contagem += 1
        soma += num
    
    else:
        parar = True
    
print("A quantidade de números digitados foi {} e a soma deles resulta em {}".format(contagem, soma))