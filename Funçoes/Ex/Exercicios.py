def reverso(numero):
    rever = ""
    for n in str(numero):
      rever = n + rever

    return rever



num = int(input("Digite um número: "))
print(f"{reverso(num)}")