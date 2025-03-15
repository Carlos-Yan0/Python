from datetime import date

ano = int(input("Digite o ano do seu nascimento: "))
idade = date.today().year - ano
ano_alistamento = 18 - idade
atrasado_alistamento = idade - 18
data_atrasado = ano + 18

if ano > date.today().year:
    print("UM VIAJANTE DO TEMPOO!!")

elif 18 > idade:
    print("Você ainda vai servir, se aliste em {} anos".format(ano_alistamento))

elif 18 == idade:
    print("Você tem que se alistar nesse ano mesmo, encontre o posto militar mais proximo.. ")

elif idade > 18:
    print("Você deveria ter se alistado em {}".format(data_atrasado))
