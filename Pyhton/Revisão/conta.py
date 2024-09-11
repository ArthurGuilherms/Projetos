class Conta():
    def __init__(self, numero, titular, saldo, limite):
        print("Criando conta...")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("A conta do títular {} possui {} de saldo\nLimite: {}".format(self.titular, self.saldo, self.limite))
    
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def pagar(self, valor):
        self.saldo -= valor
        self.limite += valor
