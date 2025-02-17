def QntNum(numero):
    quant = len(str(numero))
    return quant
    

num = int(input("Digite um número: "))
print(f"A quantidade de digitos no número {num} é {QntNum(num)}")
