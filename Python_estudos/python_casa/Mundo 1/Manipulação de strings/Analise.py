frase = "Olá mundo lindo maravilhoso"

print(len(frase)) #indica o comprimento da frase
print(frase.count("o")) #indica quantos "o" MINUSCULO(sim ele diferencia) tem na frase
print(frase.count("o", 0, 13)) #indica quantos "o" tem no espaço de 0 a 12 caracteres
print(frase.find("oso")) #indica em que localização tem "oso" na frase(sempre da primeira letra)
print(frase.find("biluteteia")) #como nao existe isso na frase ele retornara com valor -1
print("mundo" in frase) #retorna se tem mundo na frase
