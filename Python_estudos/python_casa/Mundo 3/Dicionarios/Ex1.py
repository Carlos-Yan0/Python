dicionario = dict()

dicionario["nome"] = str(input("Digite o nome do aluno: "))
dicionario["media"] = float(input(f"Digite a media de {dicionario["nome"]}: "))
print(f"Nome é igual a {dicionario["nome"]}")
print(f"Media é igual a {dicionario["media"]}")
print(f"a situação é igual a ", end = "")
if dicionario["media"] < 5:
    print("Reprovado")
elif dicionario["media"] < 7:
    print("Recuperação")
else:
    print("Aprovado")