n = int(input("Digite um número para ver se é primo: "))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        cont += 1

if cont == 1:
    primo = False
    
elif cont > 2:
    primo = False

else:
    primo = True

if(primo):
    print(f"{n} é primo")
else:
    print(f"{n} não é primo")