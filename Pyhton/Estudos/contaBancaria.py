class ContaBancaria:
    def __init__(self, titular = "", saldo = 0, ativo = False):
        self._titular = titular
        self.saldo = saldo
        self._ativo = ativo

    def __str__(self):
        return f'Titular: {self.titular.ljust(10)} | Saldo:{str(self.saldo).ljust(10)} | Situação: {self.ativo}'
    
    def ativar_conta(self):
        self._ativo = True

    @property
    def ativo(self):
        return "Ativa" if self._ativo else "Desligada"
    
    @property
    def titular(self):
        return self._titular

