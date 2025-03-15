altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite o seu peso: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso\nImc:{:.2f}".format(imc))

elif imc < 25:
    print("Peso ideal\nImc:{:.2f}".format(imc))

elif imc < 30:
    print("Sobrepeso\nImc:{:.2f}".format(imc))

elif imc < 40:
    print("Obesidade\nImc:{:.2f}".format(imc))

elif imc >= 40:
    print("Obesidade morbida\nImc:{:.2f}".format(imc))