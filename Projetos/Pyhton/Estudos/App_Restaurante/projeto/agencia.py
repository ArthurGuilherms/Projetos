from banco import Banco

class Agencia(Banco):
    def __init__(self, nome, endereco, numero):
        super().__init__(nome, endereco)
        self._numero = numero

    def __str__(self):
        return self._nome
    
agencia1 = Agencia("Nubank", "Digital", "01")
print(agencia1)
'''Já no arquivo agencia.py, vamos definir uma classe que herda da classe Banco. A herança é indicada pelo uso de parênteses na declaração da classe, indicando que a classe Agencia é uma subclasse da classe Banco.'''