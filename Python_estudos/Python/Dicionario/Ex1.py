letras = { "a": 0, "b": 0, "c": 0, "d": 0, "e": 0,
               "f": 0, "g": 0, "h": 0, "i": 0, "j": 0,
              "k": 0, "l": 0, "m": 0, "n": 0, "o": 0,
              "p": 0, "q": 0, "r": 0, "s": 0, "t": 0,
              "u": 0, "v": 0, "w": 0, "x": 0, "y": 0,
               "z": 0}

frase = str(input("Digite uma frase: ")).lower().strip()
q_letras = 0

for l in frase:
    if l in letras:
        letras[l] += 1
        q_letras += 1

letra_frequente = max(letras, key = letras.get)
letra_frequente_quantidade = letras[letra_frequente]

print(f"A frase escolhida foi: {frase}")
print(f"a quantidade total de letras da frase é {q_letras}")
print(f"A letra que mais apareceu foi '{letra_frequente}' com {letra_frequente_quantidade} ocorrências.")