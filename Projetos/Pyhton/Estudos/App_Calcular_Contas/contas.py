class Conta:
    lista_contas = []

    def __init__(self, nome):
        self._nome = nome
        self.valor = 0
        Conta.lista_contas.append(self)
    
    def __str__(self):
        return str(self._nome)
    
    def informar_valor(self, valor = float):
        self.valor = valor