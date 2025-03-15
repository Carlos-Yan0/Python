velo = int(input("Digite a velocidade do carro: "))

if velo > 80:
    multa = float((velo - 80) * 7)
    print("Você ultrapassou o limite de velocidade e será multado!!")
    print("Você terá que pagar R${} de multa".format(multa))
    
else:
    print("Dirija com segurança!!")