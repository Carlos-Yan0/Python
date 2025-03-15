nome = str(input("Digite um nome completo: ")).strip()
nome_lista = nome.split()

print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(" "))
print(len(nome_lista[0]))
