#cria uma classe chamada pessoa com atributos nome, idade, peso e altura
class pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    #cria os metodos da classe pessoa que são envelhecer, engordar, emagrecer e crescer
    def envelhecer(self, idade_add):
        if self.idade < 21:
            anos_de_crescimento = min(idade_add, 21 - self.idade)
            self.crescer(anos_de_crescimento)

        self.idade += idade_add
    
    def engordar(self, kg):
        self.peso += kg

    def emagrecer(self, kg):
        self.peso -= kg
    
    def crescer(self, anos):
        self.altura += anos * 0.05  # Cada ano cresce 5 cm



#declaração dos valores dos atributos
nome = str(input("Qual o nome da lenda: "))
idade = int(input("Qual a idade da lenda: "))
peso = float(input("Qual o peso da lenda: "))
altura = float(input("Qual a altura da lenda: "))



#cria um objeto com a classe pessoa
pessoas = pessoa(nome, idade, peso, altura)


#adiciona idade a pessoa
idade_add = int(input(f"Digite quantos anos deseja add a {pessoas.nome}: "))
pessoas.envelhecer(idade_add)

#muda o peso da pessoa
escolha = str(input("Deseja engordar ou emagrecer[I para engordar e E para emagrecer]: ")).strip().upper()[0]
if escolha in "I":
    kg = float(input("Quantos kg deseja engordar: "))
    pessoas.engordar(kg)

elif escolha in "E":
    kg = float(input("Quantos kg deseja emagrecer: "))
    pessoas.emagrecer(kg)

#cresce a pessoa até os 21
if pessoas.idade < 21:
    pessoas.crescer()


#escreve as informações na tela
print(f"nome: {pessoas.nome}\nIdade:{pessoas.idade}\nPeso:{pessoas.peso}\nAltura:{pessoas.altura}Cm")

#Teste novice