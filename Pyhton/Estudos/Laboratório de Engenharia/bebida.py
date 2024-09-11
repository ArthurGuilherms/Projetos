class Bebida:
    def __init__(self, tipo):
        self.tipo = tipo
        self.valor 

    def definir_tipo(self,tipo):
        if tipo == 1:
            self.tipo = "Refrigerante"
        if tipo == 2:
            self.tipo = "Suco"
    
    def definir_valor(self, valor):
        if valor == 1:
            self.valor = 8.00
        if valor == 2:
            self.valor = 6.00