import datetime
ano = int(input("Digite um ano e verifique se é bissexto, coloque 0 para verificar o ano atual: "))

if ano == 0:
    ano = datetime.date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano de {} é bissexto".format(ano))

else:
    print("O ano de {} nao é bissexto".format(ano))