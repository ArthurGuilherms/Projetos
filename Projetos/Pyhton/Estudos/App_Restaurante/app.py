from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante1 = Restaurante("Teta Burger's", "Hamburguer's", True, False)
bebida1 = Bebida("Refri", 7, "1L")
prato1 = Prato("Teta Burguer", 14, "O Teta Burguer tradicional e delicioso!")
sobremesa1 = Sobremesa("Pudim", 3.5, "Doce", "P")

bebida1.aplicar_desconto()
prato1.aplicar_desconto()

restaurante1.adicionar_no_cardapio(bebida1)
restaurante1.adicionar_no_cardapio(prato1)
restaurante1.adicionar_no_cardapio(sobremesa1)

def main():
    restaurante1.exibir_cardapio

if __name__ == "__main__":
    main()