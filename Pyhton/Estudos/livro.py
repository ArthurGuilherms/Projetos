class Livro():
    lista_livros = []
    def __init__(self, titulo, autor, ano_publicacao, disponivel = True):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = disponivel
        Livro.lista_livros.append(self)
    
    def __str__(self):
        return f'{self._titulo.ljust(20)} | {self._autor.ljust(20)} | {self._ano_publicacao}'
    
    def emprestar_livro(self):
        self._disponivel = False

    def verificar_disponibilidade(ano):
        disponibilidade = False
        for livros in Livro.lista_livros:
            if livros._disponivel and (ano == livros._ano_publicacao):
                disponibilidade = True
                print(livros)
        if not disponibilidade:
            return print("Indisponível")
        
'''livro1 = Livro("O Hobbit", "Tokken", 1937)
livro2 = Livro("Meditações", "Marcos Aurélio", 2019)
livro1.emprestar_livro()
print(livro1._disponivel)
Livro.verificar_disponibilidade(2029)'''

'''Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.

Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.'''