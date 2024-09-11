class Pessoa:
    def __init__(self, nome = "", idade = 0, profissao = ""):
        self.nome_ = nome
        self.idade_ = idade
        self.profissao_ = profissao

    def __str__(self):
        return f'{self.nome_} tem {self.idade_} anos e possui a profissão {self.profissao_.lower()}'

    def aniversario(self):
        self.idade_ = self.idade_ + 1
        print("Feliz aniversário!")
    
    def saudacao(self):
        if self.profissao_ == "Programador":
            return print(f'Hello World!')
        else:
            return print(f'Seja bem vindo!')

