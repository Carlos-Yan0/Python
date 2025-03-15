import random

nome_1 = str(input("Digite o nome do primeiro aluno: "))
nome_2 = str(input("Digite o nome do segundo aluno: "))
nome_3 = str(input("Digite o nome do terceiro aluno: "))
nome_4 = str(input("Digite o nome do quarto aluno: "))

lista = [nome_1, nome_2, nome_3, nome_4]
escolhido = random.choice(lista)

print("O aluno escolhido foi {}".format(escolhido))