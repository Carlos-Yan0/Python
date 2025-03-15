while True:
    num = int(input("Qual número deseja ver a tabuada(números negativos para sair): "))
    if num < 0:
        break

    elif 0 <= num:
        for c in range(1, 11):
            print(f"{num} X {c} = {num * c}")
