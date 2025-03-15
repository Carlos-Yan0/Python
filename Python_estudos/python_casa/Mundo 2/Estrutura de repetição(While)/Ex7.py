quantidade = int(input("Digite a quantidade de numeros da sequencia de fibonacci que deseja ver: "))
q = quantidade - 2
n1 = 0
n2 = 1
print("{} {}".format(n1, n2), end = " ")

while q > 0:
    if n1 == n2:
        n1 += n1
        n2 += n1
        print("{}".format(n1), end = " ")
        q -= 1

    elif n2 > n1:
        n1 += n2
        print("{}".format(n2) if quantidade > 1 else "{}".format(n2), end = " ")
        q -= 1
    
    elif n1 > n2:
        n2 += n1
        print("{}".format(n1) if quantidade > 1 else "{}".format(n1), end = " ")
        q -= 1

