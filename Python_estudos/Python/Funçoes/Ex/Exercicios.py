# cria a função para reverter o numero
def reverso(numero):

    #inicia a variavel rever com nada e inverte a ordem dos numeros
    rever = "" 
    for n in str(numero):
      rever = n + rever

    #retorna a ordem inversa
    return rever


#recebe um numero e executa a função
num = int(input("Digite um número: "))
print(f"{reverso(num)}")