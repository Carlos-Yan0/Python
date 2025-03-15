preco_casa = float(input("{}Digite o preço da casa que deseja comprar: R${}".format("\033[33m", "\033[33m")))
salario = float(input("{}Digite o salário do comprador: R${}".format("\033[34m", "\033[34m")))
anos = int(input("{}Digite em quantos anos ira parcelar a casa(sem juros):R${} ".format("\033[31m", "\033[31m")))
prestacao_maxima = salario * 0.30
prestacao_preco = preco_casa / (anos * 12)

#todas as variaveis utilizadas, tambem inseri cor no terminal atravez do format!

if prestacao_maxima <= prestacao_preco:
    print("Emprestimo negado pq vc é mendigo!!!")

else:
    print("Emprestimo aprovado!! cada parcela sera R${:.2f}".format(prestacao_preco))

#se e senao para emprestimo aprovado ou negado