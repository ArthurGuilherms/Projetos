from abc import abstractclassmethod


class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False

    def __str__(self):
        return f'O veiculo da marca {self._marca} e modelo {self._modelo} está {self.ligado}'
    
    @property
    def ligado(self):
        return "ligado" if self._ligado else "desligado"
    
    @abstractclassmethod
    def ligar(self):
        pass

"""Crie uma Classe Pai (Veiculo): Implemente uma classe chamada Veiculo com um construtor que aceita dois parâmetros, marca e modelo. A classe deve ter um atributo protegido _ligado inicializado como False por padrão.
Construa o Método Especial str: Adicione um método especial str à classe Veiculo que retorna uma mensagem formatada com a marca, modelo e o estado de ligado/desligado do veículo."""