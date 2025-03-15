parar = False
contagem = soma = 0

while parar == False:
    
    num = int(input("Digite um número: "))
    soma += num
    if contagem == 0:
        maior = num
        menor = num
    
    elif num > maior:
        maior = num
    
    elif num < menor:
        menor = num
    contagem += 1
    continuar = int(input("""Deseja continuar:
                          [1]Sim
                          [2]Não\n"""))
    
    if continuar == 1:
        parar = False
    
    elif continuar == 2:
        parar = True
    
    
print("O maior número digitado foi {}, o menor foi {} e a media dos valores digitados é {}".format(maior, menor, (soma / contagem)))