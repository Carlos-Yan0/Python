tupla = ("Caderneta", 19, "Ouro puro de ofir", 99999, "Quadradox", 923,
         "Comida", 1500, "Salvação", "Incompravel!" )

print("_" * 50)
print("\n{:-^50}".format("Lojão do papagaio"))
print("_" * 50)

for pos in range(0, len(tupla)):

    if pos % 2 == 0:
        print(f"{tupla[pos]:.<40}", end = "")

    elif pos % 2 == 1:
        print(f"R${tupla[pos]:>8.2f}")
        print("-" * 50)
    