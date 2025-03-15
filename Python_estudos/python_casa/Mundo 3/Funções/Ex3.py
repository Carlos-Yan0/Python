def contagem(i, f, p):
    if p < 0:
        p = p * p
    
    elif p == 0:
        p = 1

    print(f"Contagem começando de {i} até {f} de {p} em {p}")

    if i > f:
        while i >= f:
            print(i, end = " ", flush = True)
            i -= p
            sleep(0.5)

    elif i < f:
        while f >= i:
            print(i, end = " ", flush = True)
            i += p
            sleep(0.5)


from time import sleep

print("Contagem de 1 até 10 de 1 em 1!")
for c in range(1, 11):
    print(c, end = " ", flush = True)
    sleep(0.5)
print("Fim")
print()

print("Contagem de 10 até 0 indo de 2 em 2!")
for c in range(10, -1, -2):
    print(f"{c}", end = " ", flush = True)
    sleep(0.5)
print("Fim")
print()

print("Agora é a sua vez de fazer a contagem!")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

contagem(inicio, fim, passo)