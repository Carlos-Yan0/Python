km = int(input("Digite a distancia em km da sua viagem: "))

if km <= 200:
    preco = km * 0.50
    print("A distancia da viagem é de {} Km e o preço será de R${}".format(km, preco))
else:
    preco = km * 0.45
    print("A distancia da viagem será de {} Km e o preço será de R${}".format(km, preco))
