def escreva(a):
    print("~" * (len(a) + 2))
    print(f" {a}")
    print("~" * (len(a) + 2))


frase = str(input("Digite uma frase: "))
escreva(frase)