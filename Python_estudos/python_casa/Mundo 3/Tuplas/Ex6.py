tupla = ("Paralelepipedo", "Ornitorrinco", "Beleza", "Dog")

for c in tupla:
    print(f"{c} tem as vogais: ", end = "")
    for letra in c:
        if letra.lower() in "aeiou":
            print(letra, end = " ")
            
    print("\n")