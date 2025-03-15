from os import system, name

def limpa():
    # Limpa a tela dependendo do sistema operacional
    if name == 'nt':  # Para Windows
        system('cls')


class conta:
    numero = "00000-0"
    saldo = 0.0

    def deposito(self, valor):
        self.saldo += valor
    
    def saque(self, valor):
        if (self.saldo >= valor):
            self.saldo -= valor
        else:
            print("Saldo insuficiente")
    


if __name__ == "__main__":
    conta = conta()
    conta.saldo = 20
    conta.numero = "13131-2"
    print(conta.saldo)
    print(conta.numero)

val = float(input("Digite um valor para adicionar a conta: "))
conta.deposito(val)
print(f"Saldo:{conta.saldo}")
while True:
    while True:
        limpa()
        print(conta.saldo)
        DS = str(input("Digite (S) para sacar e (D) para depositar: ")).strip().upper()[0]
        if DS in "SD":
            break
    if DS in "S":
        val = float(input("Digite um valor para remover da conta: "))
        conta.saque(val)
    
    if DS in "D":
        val = float(input("Digite um valor para adicionar a conta: "))
        conta.deposito(val)
    cont = str(input("Deseja sair[S/N]: ")).strip().upper()[0]
    if cont in "S":
        break


print(conta.saldo)