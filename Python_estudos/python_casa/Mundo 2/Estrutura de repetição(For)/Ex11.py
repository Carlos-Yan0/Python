maioridade = 0
mulheres = 0
media = 0

for c in range(1, 5):
    print("-=" * 10, end = "")
    print("{} pessoa".format(c), end = "")
    print("-=" * 10)
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo[M/F]: \n")).strip()

    media += idade

    if idade > maioridade and sexo in "mM":
        maioridade = idade
        velho = nome
    if sexo in "fF" and idade > 20:
        mulheres += 1

print("A idade media das pessoas é de {} anos".format(media / 4))
print("O homem mais velho tem {} anos e se chama {}".format(maioridade, velho))
print("O número de mulheres acima de 20 anos é de {}".format(mulheres))
        