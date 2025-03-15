
#matriz  = list()
#vet = []
#for c in range(0, 9):
 #   vet.append(int(input("Digite um número: ")))    minha solução ai(pouco usavel, ineficiente)
 #   matriz.append(vet[:])
 #   vet.clear()
  
#for c in range(0, 9):
 #   if c == 3 or c == 6:
  #      print("\n", end = "")
   # print(f"{matriz[c]}", end = "")


#solução do guanabara, eficiente

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valora para [{l}, {c}]: "))
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end = "")
    print()