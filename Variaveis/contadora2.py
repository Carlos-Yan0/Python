n = int(input("uma quantidade de número para ser analisada: "))
print("Informe o número: ")
anterior = int(input())

i = 1
ordenado = 0

while (i < n) and (ordenado == 0):
    print("informe o número: ")
    atual = int(input())
    i = i + 1
    if (atual <= anterior):
        ordenado = ordenado + 1
    anterior = atual

if (ordenado == 0):
    print("sequencia esta ordenada")

else:
    print("Sequencia não esta ordenada!")