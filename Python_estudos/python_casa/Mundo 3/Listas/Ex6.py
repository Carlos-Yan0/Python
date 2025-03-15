#nao consegui fazer sem ver a resposta

#resposta do guanabara

expre = str(input("Digite uma expressão: "))
pilha = []

for simb in expre:
    if simb == "(":
        pilha.append(simb)
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break

if pilha == 0:
    print("Expressão valida!")
else:
    print("Expressão invalida!")


#resposta minha que eu pensei antes de ver o video(sem listas)

#expre = str(input("Digite uma expressão: "))

#qp1 = expre.count("(")
#qp2 = expre.count(")")

#if qp1 == qp2:
#    print("sua expressão é valida!")
#else:
#    print("Expressão invalida!")