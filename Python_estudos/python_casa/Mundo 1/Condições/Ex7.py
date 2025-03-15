salario = float(input("Digite o salario do funcionario: "))

if salario > 1250.00:
    salario = salario + (salario * 0.10)

else:
    salario = salario + (salario * 0.15)

print("Seu novo salario será de R${:.2f}".format(salario))