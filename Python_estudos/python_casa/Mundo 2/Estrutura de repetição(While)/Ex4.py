n = int(input("Digite um número para ver seu fatorial: "))
f = 1
c = n
print("Calculando o fatorial de {}! = ".format(n), end = "")

while c > 0:
    print("{}".format(c), end = "")
    print(" X " if c > 1 else " = ", end = "")
    f *= c
    c = c - 1
print(f)

    
    