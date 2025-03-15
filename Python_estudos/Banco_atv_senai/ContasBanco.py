from datetime import datetime
import pytz
from random import randint

class ContaCorrente(): #criação da classe ContaCorrente
    
    @staticmethod#cria um método estatico para ajudar na organização
    def _hora_data():#criação da função que verifica hora e data
        fuso_BR = pytz.timezone("Brazil/East")#pega o nosso fuso horario pela biblioteca PYTZ
        horario_BR = datetime.now(fuso_BR)#atravez das duas bibliotecas selecionadas(PYTZ e DATETIME) podemos definir o horario
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')#retorna a hora formatado para melhor visualização

    def __init__(self, nome, cpf, agencia, num_conta):#inicia os atributos nome, cpf, agencia e numero da conta
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []#cria uma lista das transações
        self._cartoes = []#cria uma lista dos cartões

    #criação dos métodos consultarSaldo, depositar e saque

    def consultarSaldo(self):#exibe o saldo na tela
        print(f"seu saldo é:{self._saldo:.2f}")
        pass

    def limite(self):#criação da função limite
        self._limite = -1000#limite estabelecido em -1000
        return self._limite#retorna o limite

    def depositar(self, valor):#recebe valor como parametro
        self._saldo += valor#add valor ao saldo
        self._transacoes.append((valor, self._saldo, ContaCorrente._hora_data()))
        pass

    def saque(self, valor):#recebe valor como parametro
        if (self._saldo - valor) < self.limite():#verifica disponibilidade de saldo para saque
            print("Você nao tem saldo o suficiente para sacar!")
            self.consultarSaldo()#exibe o saldo
        else:
            self._saldo -= valor#retira valor do saldo
            self._transacoes.append((valor, self._saldo, ContaCorrente._hora_data()))#add valor, saldo e data a lista de transações
        pass

    def consultar_historico_transacoes(self):#função de consultar transações
        print("Historico de transações")
        for transacoes in self._transacoes:#imprime todas as transações anteriores 
            print(transacoes)

    def transferir(self, valor, conta_destino):#função de transferencia de dinheiro
        self._saldo -= valor#retira valor da transferencia
        self._transacoes.append((valor, self._saldo, ContaCorrente._hora_data()))#registra a transferencia na lista de transações
        conta_destino._saldo += valor#add valor ao saldo da conta que recebeu a transferencia
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._hora_data()))#registra a transação na conta que recebeu a transação
    

class CartaoCredito(): #cria classe para cartão de credito

    @staticmethod#cria um método estatico para ajudar na organização
    def _data_hora():#criação da função que verifica hora e data
        fuso_BR = pytz.timezone("Brazil/East")#pega o nosso fuso horario pela biblioteca PYTZ
        horario_BR = datetime.now(fuso_BR)#atravez das duas bibliotecas selecionadas(PYTZ e DATETIME) podemos definir o horario
        return horario_BR#retorna a hora formatado para melhor visualização
    

    def __init__(self, titular, conta_corrente):#inicializa com os atributos numero, titular, validade
                                                #cod_seguranca, limite e conta_corrente

        self.numero = randint(100000000000, 999999999999)#gera um numero aleatorio
        self.titular = titular
        #add 4 anos apartir da data atual para ser a validade
        self.validade = "{}/{}".format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        #gera um cod aleatorio de 3 digitos
        self.cod_seguranca = "{}{}{}".format(randint(0,9), randint(0,9), randint(0,9))
        self.limite = None
        self.conta_corrente = conta_corrente
        #adiciona todos os atributos a lista cartoes
        conta_corrente._cartoes.append(self)

class Agencia():#cria uma classe agencia
    
    def __init__(self, telefone, cnpj, numero):#inicializa com os atributos telefone, cnpj e numero
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = [] #lista com os clientes
        self.caixa = 0
        self.emprestimos = [] #lista com os emprestimos
        
    def verificar_caixa(self): #função para verificar o caixa
        if self.caixa < 1000000:
            print(f"Caixa abaixo do nivel recomendado. Caixa atual:R${self.caixa}")
        else:
            print(f"O valor do caixa esta OK. Caixa atual:R${self.caixa}")

    def emprestar_dinheiro(self, valor, cpf, juros):#função para emprestar dinheiro
        if self.caixa > 1000000:
            self.emprestimos.append((valor, cpf, juros))
            print("Emprestimo efetuado!")
        else:
            print("Emprestimo negado!")

    def adicionar_cliente(self, nome, cpf, patrimonio):#função para adicionar clientes a lista criada
        self.clientes.append((nome, cpf, patrimonio))#adiciona os clientes a lista

class AgenciaVirtual(Agencia):#uma outra agencia porem herda as caracteristicas da classe mãe
    
    def __init__(self, site, telefone, cnpj, numero): #inicializa com os atributos site, telefone
                                                      #cnpj e numero
        self.site = site
        super().__init__(telefone, cnpj, numero) #herdando os atributos telefone, cnpj e numero da classe
                                                 #mãe
        self.caixa_paypal = 0

    def depositar_paypal(self, valor): #função para deposito
        self.caixa -= valor #tira valor do caixa
        self.caixa_paypal += valor #adiciona valor ao "paypal"
    
    def saque_paypal(self, valor):#função de saque
        self.caixa += valor #adiciona valor ao caixa
        self.caixa_paypal -= valor #retira valor do "paypal"

    def adicionar_cliente(self, nome, cpf, patrimonio):
        super().adicionar_cliente(nome, cpf, patrimonio) 


class AgenciaComum(Agencia):#agencia comum herdando a classe AGENCIA
    
    def __init__(self, telefone, cnpj, numero):#inicializa com esses atributos
        super().__init__(telefone, cnpj, numero)#herda esses atributos
        self.caixa = 1000000
    
    def adicionar_cliente(self, nome, cpf, patrimonio):
        super().adicionar_cliente(nome, cpf, patrimonio)#pega a função adicionar_cliente da classe mae

class AgenciaPremium(Agencia):#terceira agencia que herda caracteristicas da classe mae

    def __init__(self, telefone, cnpj, numero):#inivializa com esses atributos
        super().__init__(telefone, cnpj, numero)#herda esses atributos
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)#pega a função adicionar_cliente da classe mae
        else:
            print("Cliente não possui o patrimonio minimo necessario")#caso nao tenha patrimonio o suficiente

