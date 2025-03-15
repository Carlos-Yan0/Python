#cria a função potencia
def potencia(a, b):

    #res começa com 1 pois toda potencia elevada a 0 é 1
    res = 1

    #faz o Calculo de potencia
    for c in range(b):
        res *= a
    
    #retorna res
    return res



#recebe as variaveis e escreve o resultado da potenciação na tela
num1 = int(input("Digite um número: "))
num2 = int(input("Digite a quantidade de vezes que deseja elevar o primeiro número: "))

print(f"{num1} elevado a {num2} é {potencia(num1, num2)}")