
class Pessoa:

    def __init__(self, nome):
        self.nome = nome

    def getNome(self):
        return "%s" % (self.nome)