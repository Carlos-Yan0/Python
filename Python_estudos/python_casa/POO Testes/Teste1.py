class banco():
    def __init__(self):
        self.saldo = 0.0
        self.saldo_investimentos = 0.0
        self.Renda_fixa = 0.0
        self.FIIS = 0.0
        self.acoes = 0.0

    def saque(self, retirada):
            if retirada > self.saldo:
                print("saldo insuficiente!")
            else:
                self.saldo -= retirada
    
    def deposito(self, deposito):
        self.saldo += deposito
    
    def investimentos(self):
        while True:
            esc = int(input("[1]Renda Fixa\n[2]FIIS\n[3]Ações\n[4]tirar dinheiro\n[5]sair"))
            match esc:
                case 1:
                    inv = float(input("Deseja investir quanto em Renda Fixa: "))
                    self.saldo_investimentos += inv
                    self.Renda_fixa += inv
                case 2:
                    inv = float(input("Quanto deseja investir em FIIS: "))
                    self.saldo_investimentos += inv
                    self.FIIS += inv
                case 3:
                    inv = float(input("Quanto deseja investir em ações: "))
                    self.saldo_investimentos += inv
                    self.acoes += inv
                case 4:
                    while True:
                        esc2 = int(input("Deseja vender\n[1]ações\n[2]Renda fixa\n[3]FIIS\n[4]sair"))
                        match esc2:
                            case 1:
                                retirar = float(input("Quanto deseja retirar das ações:"))
                                if retirar > self.acoes:
                                    print("valor indisponivel tente novamente")
                                else:
                                    self.saldo_investimentos -= retirar
                                    self.acoes -= retirar 
                            case 2:
                                retirar = float(input("Quanto deseja retirar da Renda fixa:"))
                                if retirar > self.Renda_fixa:
                                    print("valor indisponivel tente novamente")
                                else:
                                    self.saldo_investimentos -= retirar
                                    self.Renda_fixa -= retirar
                            case 3:
                                retirar = float(input("Quanto deseja retirar dos FIIS:"))
                                if retirar > self.FIIS:
                                    print("valor indisponivel tente novamente")
                                else:
                                    self.saldo_investimentos -= retirar
                                    self.FIIS -= retirar
                            case 4:
                                print("Saindo..")
                                break

                case 5:
                    print("Voltando..")
                    break

bank = banco()
bank.deposito(1000)

import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_terminal()
print("Bem vindo ao banco senbozakura kagueioshi, o que gostaria de fazer")
while True:
    esc3 = int(input("[1]ver saldo\n[2]investir\n[3]sacar\n[4]depositar\n[5]Sair\n"))
    limpar_terminal()
    match esc3:
        case 1:
            print(f"Seu saldo é de R${bank.saldo}")
        case 2:
            bank.investimentos()

        case 3:
            sacar = float(input("Quanto deseja sacar: "))
            bank.saque(sacar)

        case 4:
            deposito = float(input("Quanto deseja depositar: "))
            bank.deposito(deposito)

        case 5:
            break
