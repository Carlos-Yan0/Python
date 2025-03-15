frase = str(input("Digite alguma coisa e veja se é um palindromo: ")).upper().strip()
palavras = frase.split()
junto = "".join(palavras)
palindromo = junto[::-1]

if junto == palindromo:
    print(f"{frase} é um palindromo!")
else:
    print("teve avc")