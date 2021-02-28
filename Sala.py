from Pessoa import Pessoa

class Sala:

    def __init__(self, nome, lotacao_limite):
        self.nome = nome
        self.lotacao_limite = lotacao_limite
        self.pessoas = []

    def getNome(self):
        return self.nome

    def getLotacao(self):
        return len(self.pessoas)

    def addPessoa(self, pessoa: Pessoa):
        # Se a pessoa já está na lista, printa a mensagem e quebra co dódigo aqui
        if pessoa in self.pessoas:
            print ("%s já está na sala %s." % (pessoa.getNome(), self.nome))
            return
        if len(self.pessoas) >= self.lotacao_limite:
            print ("%s não pode entrar na sala %s, pois a mesma está cheia." % (pessoa.getNome(), self.nome))
            return
        # Se a pessoa nãoe stá na lista, adiciona a pessoa
        self.pessoas.append(pessoa)
        print("%s entrou na sala %s. Lotação atual: %s." % (pessoa.getNome(), self.nome, len(self.pessoas)))

    def removePessoa(self, pessoa: Pessoa):
        # Se a pessoa não está na lista, printa a mensagem e quebra co dódigo aqui
        if pessoa not in self.pessoas:
            print ("%s não está na sala %s." % (pessoa.getNome(), self.nome))
            return
        self.pessoas.remove(pessoa)
        print("Pessoa %s removida da sala %s. Lotação atual: %s" % (pessoa.getNome(), self.nome, len(self.pessoas)))