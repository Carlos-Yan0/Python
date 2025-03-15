print("{:=^40}".format("Lojas Yan") )
preco_n = float(input("Digite o preço do produto: "))

escolha  = int(input("""1. A vista no dinheiro/cheque
2. A vista no cartão
3. 2X no cartão
4. 3X ou mais no cartão\n"""))

if escolha == 1:
    print("A vista(Dinheiro/cheque) esse produto ficaria R${:.2f}".format(preco_n - (preco_n * 0.10)))

elif escolha == 2:
    print("A vista(cartão) esse produto ficaria R${:.2f}".format(preco_n - (preco_n * 0.05)))

elif escolha == 3:
    print("Em até duas vezes no cartão esse produto ficaria R${:.2f}".format(preco_n))

elif escolha == 4:
    print("3X ou mais esse produto ficaria R${:.2f}".format(preco_n + (preco_n * 0.20)))

else:
    print("Opção invalida!")