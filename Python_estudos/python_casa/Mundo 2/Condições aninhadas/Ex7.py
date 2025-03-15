r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:

    if r1 == r2 == r3:
        print("Os três segmentos formam um triangulo equilatero!")
    
    #elif r1 == r2 and r1 != r3 or r1 != r2 and r1 == r3 or r2 == r3 and r2 != r1:
       # print("Os três segmentos formam um triangulo isosceles!")

    elif r1 != r2 != r3 != r1:
        print("Os três segmentos formam um triangulo escaleno!")
    
    else:
        print("Os três segmentos formam um triangulo isosceles!")

else:
    print("Os segmentos não formam um triangulo")