class Conta(object):

    # Ever start variables
    saldo = 0

    # Getters and Setters
    def Depositar(self, valor):
        self.saldo += valor

    def Sacar(self, valor):
        self.saldo -= valor

    def getSaldo(self):
        return self.saldo

    def MostrarSaldo(self):
        print("Esse é o seu saldo atual: R$", self.getSaldo())


# Instacia da classe Conta
obj = Conta()
obj.Depositar(1000)


# Conta poupança que herda atributos e classes de conta
class ContaPoupanca(Conta):

    def MostrarSaldoPoupanca(self):
        print("Esse é o seu saldo atual: R$", self.getSaldo())

    # Instancia da classe ContaPoupança que herda também os objetos de Conta
    # obj.Depositar(1000)
    # obj.MostrarSaldo()


# Instância dos metodos herdados de ContaPoupanca que herda Conta(Aplicação do polimorfismo)
obj_poupanca = ContaPoupanca()
obj_poupanca.Depositar(1100)
obj_poupanca.MostrarSaldoPoupanca()