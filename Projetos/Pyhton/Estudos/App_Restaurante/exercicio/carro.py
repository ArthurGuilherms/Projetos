from exercicio.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas = 0):
        super().__init__(marca, modelo)
        self._portas = portas

    def __str__(self):
        return f'{str(super().__str__())} e possui {self._portas} portas'
    
    def ligar(self):
        self._ligado = True

'''Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo. No construtor da classe Carro, inclua um novo atributo chamado portas que indica a quantidade de portas do carro.
Implemente o Método Especial str na Classe Filha: Adicione um método especial str à classe Carro que estenda o método da classe pai (Veiculo) e inclua a informação sobre a quantidade de portas do carro.'''