#Class
class Pessoa(object):
    nome = 'Oscar'

    def __int__(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def printNome(self):
        print("O nome é:", self.getNome())


obj = Pessoa()
obj.setNome("Oscar da Silva")

obj.printNome()