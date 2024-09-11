class Pizza:
    # Variável de classe para verificar se uma pizza está em produção
    producao = False

    def __init__(self, sabor, tamanho):
        # Inicializa a pizza com sabor, tamanho e preço definido automaticamente
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco = self.definir_preco()
        self.lista_opnioes = []  # Lista para armazenar opiniões sobre a pizza
        self.notas_avaliacoes = []  # Lista para armazenar as notas de avaliações da pizza

    # Define o preço da pizza com base no tamanho escolhido
    def definir_preco(self):
        if self.tamanho in ["p", "P"]:
            return 22.99
        elif self.tamanho in ["m", "M"]:
            return 25.99
        elif self.tamanho in ["g", "G"]:
            return 29.99
    
    # Método para iniciar a produção da pizza
    def produzir(self):
        Pizza.producao = True

    # Método para cancelar a produção da pizza
    def cancelar(self):
        Pizza.producao = False

    # Método para avaliar a pizza
    def avaliar(self):
        nota = input("Nota:")
        self.notas_avaliacoes.append(nota)
        opiniao = input("Escreva sua opinião:")
        self.lista_opnioes.append(opiniao)
