class Pizza:
    producao = False
    def __init__(self, sabor, tamanho):
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco = self.definir_preco()
        self.lista_opnioes = []
        self.notas_avaliacoes = []

    def definir_preco(tamanho):
        if tamanho == "p" or "P":
            return 22.99
        if tamanho == "m" or "M":
            return 25.99
        if tamanho == "g" or "G":
            return 29.99
    
    def produzir(self):
        Pizza.producao = True

    def cancelar(self):
        Pizza.producao = False

    def avaliar(self):
        nota = input("Nota:")
        self.notas_avaliacoes.append(nota)
        opiniao = input("Escreva sua opinião:")
        self.lista_opnioes.append(opiniao)