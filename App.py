from Pessoa import Pessoa
from SalaEvento import SalaEvento
from SalaCafe import SalaCafe

class App: 

    def __init__(self):
        self.salas = []

    def criarSala(self, nome, tipo, lotacao_limite):
        if tipo == "evento":
            sala = SalaEvento(nome, lotacao_limite)
        elif tipo == "cafe":
            sala = SalaCafe(nome, lotacao_limite)

        if not sala in self.salas:
            self.salas.append(sala)

        print("Sala %s criada com sucesso." % nome)
        return sala

    def criarPessoa(self, nome):
        pessoa = Pessoa(nome)
        print("Pessoa %s criada com sucesso." % nome)
        return pessoa

    def printSalas(self):
        for sala in self.salas:
            print("Sala: %s, lotação: %s" % (sala.getNome(), sala.getLotacao()))

app = App()

#------ CRIANDO SALAS ------
print("\nCriando salas:\n")

sala1 = app.criarSala("Evento 1", "evento", 3)
sala2 = app.criarSala("Evento 2", "evento", 3)
cafe1 = app.criarSala("Cafe 1", "cafe", 3)
cafe2 = app.criarSala("Cafe 2", "cafe", 3)

#------ CRIANDO PESSOAS ------
print("\nCriando pessoas:\n")

jose = app.criarPessoa("jose")
maria = app.criarPessoa("maria")
andreia = app.criarPessoa("andreia")
marcus = app.criarPessoa("marcus")
jaine = app.criarPessoa("jaine")
xande = app.criarPessoa("xande")

#------ ADICIONANDO PESSOSAS NA SALA 1 ------
print("\nAdicionando pessoas na sala1:\n")

sala1.addPessoa(jose)
sala1.addPessoa(maria)
sala1.addPessoa(andreia)

#------ ADICIONANDO PESSOSAS NA SALA 2 ------
print("\nAdicionando pessoas na sala2:\n")

sala2.addPessoa(xande)
sala2.addPessoa(jaine)
sala2.addPessoa(marcus)

print("\nResumo das salas:\n")

app.printSalas()

#------ REMOVENDO PESSOSAS DA SALA 1 ------
print("\nRemovendo pessoas na sala1:\n")

sala1.removePessoa(maria)
sala1.removePessoa(jose)
sala1.removePessoa(andreia)

#------ ADICIONANDO PESSOSAS DA SALA 1 NA SALA CAFE 1 ------
print("\nAdicionando pessoas que estavam na sala1 na sala cafe1:\n")

cafe1.addPessoa(maria)
cafe1.addPessoa(jose)
cafe1.addPessoa(andreia)

print("\nResumo das salas:\n")

app.printSalas()

#------ REMOVENDO PESSOSAS DA SALA 2 ------
print("\nRemovendo pessoas na sala2:\n")

sala2.removePessoa(xande)
sala2.removePessoa(jaine)
sala2.removePessoa(marcus)

#------ ADICIONANDO PESSOSAS DA SALA 2 NA SALA CAFE 2 ------
print("\nAdicionando pessoas que estavam na sala2 na sala cafe2:\n")

cafe2.addPessoa(xande)
cafe2.addPessoa(jaine)
cafe2.addPessoa(marcus)

print("\nResumo das salas:\n")

app.printSalas()

input("Digite qualquer coisa para encerrar a visualização.")
