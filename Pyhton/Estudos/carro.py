class Carro():
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = int(ano)
    
    def __str__(self):
        return f'O carro é um {self.modelo} {self.cor} {self.ano}.'