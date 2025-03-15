matriz = [[0 for _ in range(3)] for _ in range(3)] #cria uma lista com outras 3 listas cada uma com 3 valores
naoNulo = 0

for i in range(3):#pega uma lista isolada dentre as 3 listas
    for j in range(3):#pega um valor de dentro da lista selecionada
        try:#tenta executar algo
            #adiciona um valor a posição selecionada da matriz
            valor = int(input(f"Digite um valor para a posição {i}x{j} da matriz: "))
            matriz[i][j] = valor
            #verifica se o numero é nulo
            if valor != 0:
                naoNulo += 1
        except ValueError: #caso nao consiga executar o TRY ele dara essa mensagem e considerará o valor nulo
            print("Valor invalido, considerado nulo")

print("\n" * 5)
#matriz formatada de forma agradevel, sem [] "" ou ,
for linha in matriz:
    print(" ".join(f"{num:3}" for num in linha)) 
print(f"O número de números nao nulos é: {naoNulo}")
