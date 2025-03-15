dados = list()
alunos = list()

while True:
    alunos.append(str(input("Digite o nome do aluno: ")))
    alunos.append(float(input("Digite a nota 1 do aluno:")))
    alunos.append(float(input("Digite a nota 2 do aluno: ")))
    alunos.append((alunos[1] + alunos[2]) / 2)
    dados.append(alunos[:])
    alunos.clear()
    conti = str(input("Deseja continuar[S/N]: ")).strip().upper()[0]
    if "N" in conti:
        break

print("No.     Nome             média")
print("-" * 30)
for i, a in enumerate(dados):
        print(f"{i:<}     {a[0]:^8}          {a[3]:>6}")
escolha = 0
while escolha != 999:
    escolha = int(input("Digite o número do aluno para ver suas notas(999 para parar): "))
    if escolha != 999:
        print(f"O aluno {dados[escolha][0]} tirou [{dados[escolha][1]}] e [{dados[escolha][2]}]")
print("Obrigado por usar nosso programa!!")
