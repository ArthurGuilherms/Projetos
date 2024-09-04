from modelos.avaliacao import Avaliacao
from modelos.cardapio.itens_cardapio import ItemCardapio
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, delivery = False, cupons = False, situação = False):
        self.nome = nome
        self.categoria = categoria
        self._ativo = situação
        self.delivery = delivery
        self._cupons = cupons
        self.lista_avaliacoes = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    
    def __str__(self):
        return f'Resturante {self.nome} | Categoria : {self.categoria} | Situação : {self.ativo} | Cupons : {self.cupons}'
    
    def listar_restaurantes():
        print(f'{"Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Atividade".ljust(25)}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_restaurante()).ljust(25)} | {restaurante.ativo}')
    
    @property 
    def ativo(self):
        return "Ativo" if self._ativo else "Inativo"
    
    @property
    def cupons(self):
        return "Possui" if self._cupons else "Não possui"
    
    def alternar_estado(self):
        self._ativo = not self._ativo
    
    def avaliar_restaurante(self, nome, nota):
        verifica_nota = nota
        if (0 <= verifica_nota <= 5):
            nova_avaliacao = Avaliacao(nome, nota)
            self.lista_avaliacoes.append(nova_avaliacao)
        else:
            print("O valor da nota deve ser entre 0 e 5")
            
    
    def mostrar_avaliacoes(self):
        if not self.lista_avaliacoes:
            return print("Não há avaliações")
        else:
            numero_avaliacoes = 0
            while numero_avaliacoes != len(self.lista_avaliacoes):
                print(self.lista_avaliacoes[numero_avaliacoes])
                numero_avaliacoes += 1

    def media_restaurante(self):
        if not self.lista_avaliacoes:
            return "Ainda não há avaliações"
        else:
            numero_avaliacoes = 0
            soma = 0
            while numero_avaliacoes != len(self.lista_avaliacoes):
                soma += Avaliacao.pegar_nota(self.lista_avaliacoes[numero_avaliacoes])
                numero_avaliacoes += 1
            resultado = (soma / numero_avaliacoes)
            return round(resultado, 1)

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self.nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i} - {item._nome.ljust(20)} - Descrição: {item.descricao.ljust(19)} {("- R$" + str(item._preco)).rjust(12)}'
                print(mensagem_prato)
            if hasattr(item, 'tamanho') and not hasattr(item, 'tipo'):
                mensagem_bebida = f'{i} - {item._nome.ljust(20)} - Tamanho: {str(item.tamanho).ljust(41)} {("- R$" + str(item._preco)).rjust(12)}'
                print(mensagem_bebida) 
            if hasattr(item, 'tipo') and hasattr (item, 'tamanho'):
                mensagem_sobremesa = f'{i} - {item._nome.ljust(20)} - Tipo: {str(item.tipo).ljust(43)} {("- R$" + str(item._preco)).rjust(12)}'
                print(mensagem_sobremesa) 
    
    