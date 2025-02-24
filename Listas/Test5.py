notas = []
n = int(input("Entre com o numero de notas: "))
for i in range(n):
    dado = float(input(f"entre com a nota {i + 1}: "))
    notas.append(dado)
print(notas)