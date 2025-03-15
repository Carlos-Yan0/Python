maioridade = qhomens = maior_mulheres = 0
while True:
    idade = int(input("Digite a idade da pessoa: "))
    if idade >= 18:
        maioridade += 1
    
    while True:
        sexo = str(input("M/F: ")).strip().upper()[0]
        if sexo in "M":
            qhomens += 1
            break

        elif sexo in "F" and idade < 20:
            maior_mulheres += 1
            break
    
    
    continuar = str(input("Deseja continuar[S/N]: ")).strip().upper()[0]
    if continuar in "N":
        break
    
    elif continuar in "S":
        print("~" * 40)

print(f"A quantidade de pessoas com mais de 18 anos é de {maioridade}")
print(f"A quantidade de homens foi de {qhomens}")
print(f"A quantidade de mulheres com menos de 20 anos é de {maior_mulheres}")