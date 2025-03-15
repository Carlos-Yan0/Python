num = int(input("Digite um número: "))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        total += 1

if total == 2:
    print("Seu número não é primo")

else:
    print("Seu número é primo")