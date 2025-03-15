from ContasBanco import CartaoCredito, ContaCorrente, Agencia, AgenciaVirtual
from ContasBanco import AgenciaPremium, AgenciaComum
import os
from random import randint

'''para melhor compreensão foi criada a função LIMPA() que vai limpar o terminal de execução,
as funções limpa() estão como comentarios em partes especificas do codigo, caso esteja com problemas
em visualizar o codigo, ative elas'''
def limpa(): 
    os.system("cls") 
#programa

#instaciando objetos
conta_yan = ContaCorrente("Yan", "130.999.160-05", "12445", "8922430")
conta_luis = ContaCorrente("Luis", "040.139.600-02", "75319", "912341")

#depositar dinheiro
conta_yan.depositar(1000)
conta_yan.consultarSaldo()

#sacando dinheiro
conta_yan.saque(250)
conta_yan.consultarSaldo()
conta_yan.consultar_historico_transacoes()
conta_yan.transferir(200, conta_destino = conta_luis)
cartao_yan = CartaoCredito("Yan", conta_yan)
print(cartao_yan.numero,
      cartao_yan.titular,
      cartao_yan.validade,
      cartao_yan.cod_seguranca,
      cartao_yan.limite)

print(cartao_yan.__dict__)

#limpa() 

#fazendo emprestimos e verificando o caixa do banco
agencia1 = Agencia(22223333, 200000000, 4568)

agencia1.caixa = 10000000

print(agencia1.__dict__)
agencia1.verificar_caixa()
agencia1.emprestar_dinheiro(10, 11122233344, 0.1)

agencia1.adicionar_cliente("Yan", 132509524711, 100000)
print(agencia1.clientes)

#limpa()
#verificando o caixa de um banco "filho" como agencia virtual
agencia_virtual = AgenciaVirtual("www.agencia_virtual.com.br@yahoobrasil.wisx", 22224444, 152000000000, 99912312)
agencia_virtual.verificar_caixa()
print(agencia_virtual.__dict__)

#limpa()
#verificando o caixa de um banco "filho" como agencia comum
agencia_comum = AgenciaComum(33334444, 222000000000000, randint(1001, 9999))
agencia_comum.verificar_caixa()
print(agencia_comum.__dict__)

#limpa()
#verificando o caixa de um banco "filho" como agencia Premium
agencia_premium = AgenciaPremium(333333333, 3000000000, randint(1001, 9999))
print("Agencia premium: ")
print(agencia_premium.__dict__)

#limpa()
#testando a função "paypal" da agencia virtual
agencia_virtual.depositar_paypal(2000)
print(agencia_virtual.caixa)
print(agencia_virtual.caixa_paypal)

#limpa()
#testando adicionar clientes de todos as agencias
agencia1.adicionar_cliente("yan", 1111111111111, 1000000)
print(f"clientes agencia1: {agencia1.clientes}")

agencia_virtual.adicionar_cliente("yan", 1111111111111, 1000000)
print(f"clientes agencia virtual: {agencia_virtual.clientes}")

agencia_comum.adicionar_cliente("yan", 1111111111111, 1000000)
print(f"clientes agencia comum: {agencia_comum.clientes}")

agencia_premium.adicionar_cliente("yan", 111111111111, 1000000)
print(f"clientes agencia premium: {agencia_premium.clientes}")

