matriz = [[" " for _ in range(3)] for _ in range(3)]#cria uma lista com 3 listas e em cada uma 3 valores(matriz 3x3)

#essa função verifica se a posição em que o jogador decidiu jogar ja nao esta em uso
def verificar_jogada(a, b):
    return matriz[b][a] in ["X", "O"] #retorna verdadeiro

#função que verifica a vitoria do jogador
def verificar_vitoria(simbolo):
    for i in range(3):
        if all(matriz[i][j] == simbolo for j in range(3)):#se todas(all) as posições da matriz tiverem
            return True                                   # o mesmo simbolo retorna verdadeiro
                                                          #verifica linhas
        
        if all(matriz[j][i] == simbolo for j in range(3)):#se todas(all) as posições da matriz tiverem
            return True                                   # o mesmo simbolo retorna verdadeiro
                                                          #verifica colunas
        
    if all(matriz [i][i] == simbolo for i in range(3)):#se todas(all) as posições da matriz tiverem
            return True                                   # o mesmo simbolo retorna verdadeiro
       
        
    if all(matriz[i][2 - i] == simbolo for i in range(3)):#se todas(all) as posições da matriz tiverem
            return True                                   # o mesmo simbolo retorna verdadeiro
        
#mostra o tabuleirona tela, ja formatado
def tabuleiro():
    for linha in matriz:
        print("|".join(f"{elem:3}" for elem in linha))

    
turno = 0
#enquanto verdadeiro vai ficar alternando entre os jogadores
while True:
    tabuleiro()
    jogador = "X" if turno % 2 == 0 else "O"

    #enquanto verdadeiro ira jogar
    while True:
        print(f"Vez de {jogador}")#indica o jogador da vez
        #define a linha e a coluna que os jogadores irão jogar
        player_linha = int(input("Digite a linha que deseja fazer sua jogada: ")) - 1  
        player_coluna = int(input("Digite a coluna que deseja fazer sua jogada: ")) - 1
        
        #verifica a jogada para ver se a posição nao é repetida, caso seja dara erro
        verifica = verificar_jogada(player_coluna, player_linha)
        if verifica == False:
            matriz[player_linha][player_coluna] = jogador
            break
        else:
            print("Tente novamente, esse espaço ja esta sendo utilizado")

    #verifica a vitoria do jogador, indicando quem venceu e o parabenizando
    vitoria = verificar_vitoria(jogador)
    if vitoria == True:
        print(f"Parabens, o jogador '{jogador}' venceu!")
        break

    #indica se o jogo empatou
    if turno == 8:
        print("Empate!")
        break
    
    #add um ao turno
    turno += 1