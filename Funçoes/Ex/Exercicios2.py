#cria a função para contar a quantidade de digitos
def QntNum(numero):

    #pega a quantidade de digitos pela função LEN
    quant = len(str(numero))

    #retorna a quantidade de digitos
    return quant
    

#recebe o número e executa a função QntNum
num = int(input("Digite um número: "))
print(f"A quantidade de digitos no número {num} é {QntNum(num)}")
