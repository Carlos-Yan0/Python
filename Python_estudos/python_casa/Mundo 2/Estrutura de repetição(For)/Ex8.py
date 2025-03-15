frase = str(input("Digite uma frase: ")).upper().strip()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""

inverso = junto[::-1]

#for letra in range(len(junto) - 1, -1, -1):
 # inverso += junto[letra]

print(junto, inverso)

if junto == inverso:
  print("Sua frase é um Palindromo!")

else:
  print("Sua frase não é um Palindromo!")