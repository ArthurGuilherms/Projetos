class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota
    
    def __str__(self):
        return f'O cliente {self._cliente} deu nota {self._nota}'

    def pegar_nota(self):
        return self._nota