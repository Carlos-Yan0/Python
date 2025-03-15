primeiro_termo = int(input("Digite o primeiro termo da progressao aritmetica: "))
razao = int(input("Digite a razão da progressao aritmetica: "))
decimo = primeiro_termo + (10 - 1) * razao

for c in range(primeiro_termo, decimo + 1, razao):
    print(c, end = " -> ")
print("Cabo")