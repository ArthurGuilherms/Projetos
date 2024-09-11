class Bebida:
    def __init__(self, tipo):
        # Inicializa a bebida com tipo e valor
        self.tipo = tipo
        self.valor = None

    # Define o tipo da bebida com base na escolha do usuário
    def definir_tipo(self, tipo):
        if tipo == 1:
            self.tipo = "Refrigerante"
        elif tipo == 2:
            self.tipo = "Suco"
    
    # Define o valor da bebida com base no tipo escolhido
    def definir_valor(self, valor):
        if valor == 1:
            self.valor = 8.00
        elif valor == 2:
            self.valor = 6.00
