texto = input("Digie um texto: ")
pontuacao = [".", ",", ":", ";", "!", "?"]

for p in pontuacao:
    texto = texto.replace(p, " ")

numero_palavras = len(texto.split())
print(f"numero de palavras:{numero_palavras}")