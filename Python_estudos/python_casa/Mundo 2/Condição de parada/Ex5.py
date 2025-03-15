print("-" * 40)
print("              LOJA DO RATÃO")
print("-" * 40)

produtos_caros = soma = cont = 0
while True:
    produto = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço do produto: "))
    soma += preco
    cont += 1

    if cont == 1:
        menor_preco = preco
        menor_nome = produto
    
    elif menor_preco > preco:
        menor_preco = preco
        menor_nome = produto

    if preco > 1000:
        produtos_caros += 1

    valida = True
    while valida == True:
        continuar = str(input("Deseja continuar[S/N]: ")).strip().upper()[0]

        if continuar in "S":
            print("~" * 40)
            valida = False
            

        elif continuar in "N":
            valida = False

        else:
            print("Tente novamente")

    if continuar in "N":
        break

print(f"O total da compra é {soma:.2f}")
print(f"Temos {produtos_caros} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {menor_nome} e custou R${menor_preco}")