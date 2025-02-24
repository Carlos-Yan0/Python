matriz = [["O" for _ in range(4)] for _ in range(12) ] #cria uma matriz cheia de "O" indicando os assentos
                                                       #tera 12 listas com 4 elementos cada
import os #importa a biblioteca OS
#usando a biblioteca OS limpa o terminal com a função limpa
def limpa():
    os.system('cls')

#mostra os assentos do onibus ja com a formatação
def onibus():
    for i in range(12):
        print(f"{i + 1} - ", end = "")
        for j in range(4):
            if j == 1: #se j que indica as colunas estiver em 1(metade) ele usara um | para separar
                       #esquerda e direita do onibus
                print(f"{matriz[i][j]}|", end = "")
            else:
                print(f"{matriz[i][j]}", end = "")
        print()

#a linha, b coluna
def assento(a, b):
    matriz[a][b] = "X" #muda a posição de vago para ocupado no onibus
    return matriz[a][b] #retorna a posição



print("Olá, esses são os assentos do nosso onibus, os assentos disponiveis estão marcados em 'O'")
onibus()
while True:
    esc = int(input("[1]Comprar assento\n[2]sair\n"))#variavel esc para sair ou comprar assentos
    limpa() #limpa o terminal
    match esc:#escolha caso para 1 comprar e 2 sair
        case 1:
            onibus() #mostra os assentos
            #define linha e coluna a serem compradas
            linha = int(input("Escolha a linha do assento: ")) - 1
            coluna = int(input("Escolha a coluna do assento:  ")) - 1
            assento(linha, coluna) #executa a função assento
            limpa() #limpa o terminal
            print(f"Você comprou o assento {linha + 1}X{coluna + 1}") #indica o assento comprado
            onibus()

        #caso o usuario digite 2 para sair o programa se encerra
        case 2: 
            break
