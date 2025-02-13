n = int(input("Numero: "))
print(f"Informe um numero")
anterior =int(input())
i = 1 #leu um numero
ordenado = True #ordenado é a variavel indicadora
while (i < n) and (ordenado):
    atual = int(input(f"Informe um numero: "))
    i+=1
    
    if (atual < anterior):
        ordenado = False
    anterior = atual

if (ordenado):
    print("Sequencia ordenada")
else:
    print("Desordenada")