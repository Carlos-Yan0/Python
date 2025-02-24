#cria a variavel n
n = int(input("Digite um número: "))
#cria uma lista com numeros
numeros = list()

#atribui a lista numeros os numeros ATÉ a variavel n
for num in range(1, n + 1):
    numeros.append(num) #add a lista

for l in range(1, n + 1):#um for para cada linha da "escadinha"
    for c in range(l):#um for que da print de acordo com o número da linha
        print(numeros[c], end = " ") #print com espaço
    print()#pula linha
