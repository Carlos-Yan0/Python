from datetime import date
dados = dict()
ano_atual = date.today().year
dados["nome"] = str(input("Digite seu nome: "))
dados["idade"] = int(input("Digite sua idade: "))
dados["ctps"] = int(input("Carteira de trabalho(0 não tem): "))
if dados["ctps"] != 0:
    dados["ano_contratacao"] = int(input("Ano de contratação: "))
    dados["salario"] = float(input("Salarío: "))
    dados["aposentar"] = (dados["ano_contratacao"] + 35) - (ano_atual - dados["idade"])
    for k, v in dados.items():
        print(f"{k} tem o valor {v}")
else:
    for k, v in dados.items():
        print(f"{k} tem valor {v}")