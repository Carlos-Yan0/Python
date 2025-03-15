print("=-" * 20)
print("{:^40}".format("CAIXA DO YAN"))
print("-=" * 20)
print("\n")

valor = int(input("Qual valor você quer sacar: "))
total = valor
q50 = q20 = q10 = q1 = 0

if total >= 50:

    while total >= 50:
        total -= 50
        q50 += 1

if total >= 25:
    
    while total >= 20:
        q20 += 1
        total -= 20

if total >= 10:

    while total >= 10:
        q10 += 1
        total -= 10

if total >= 1:

    while total >= 1:
        q1 += 1
        total -= 1

if q50 > 0:
    print(f"Total de {q50} cedulas de R$50")

if q20 > 0:
    print(f"Total de {q20} cedulas de R$20")

if q10 > 0:
    print(f"Total de {q10} cedulas de R$10")

if q1 > 0:
    print(f"Total de {q1} cedulas de R$1")
