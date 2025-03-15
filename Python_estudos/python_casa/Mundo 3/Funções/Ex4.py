def maior(*num):
    cont = 0
    for valores in num:
        if cont == 0:
            maior = valores
        else:
            if valores > maior:
                maior = valores
        cont += 1
    print(f"dentre os {cont} numeros o maior é {maior}")



maior(0, 4, 8, 10, 99, 2)
maior(123, 17253, 1, 8, 5)