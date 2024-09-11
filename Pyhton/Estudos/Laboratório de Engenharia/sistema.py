from pizza import Pizza
from usuario import Usuario
from bebida import Bebida


class Sistema:
    def __init__(self):
        self.login = False
        self.usuarios = []
        self.pedidos = []
        self.opinioes = []

def main():
    sistema = Sistema()
    usuario = Usuario()
    
    print("Bem vindo ao menu!")

    Usuario.logar(usuario)
    while True:
        print("\n1- Fazer Pedido")
        print("2- Cadastrar Usuário")
        print("3- Cancelar Pedido")
        print("4- Opinar")
        print("5- Sair")
        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            if Pizza.producao == False:
                while True:
                    print("\nQual o tamanho da pizza? (P/M/G)")
                    print("P = R$22,99")
                    print("M = R$25,99")
                    print("G = R$29,99")
                    tamanho = input("\n>")
                    if tamanho == "P" or tamanho == "p" or tamanho == "M" or tamanho == "m" or tamanho == "G" or tamanho == "g":
                        while True:
                            print("\nQual sabor desejado?")
                            print("1- Marguerita")
                            print("2- Portuguesa")
                            print("3- Moda da Casa")
                            print("4- Cheddar com Bacon")
                            sabor = input("\n>")
                            print(sabor)
                            if sabor == "1" or sabor == "2" or sabor == "3" or sabor == "4":
                                if sabor == 1:
                                    sabor = "Marguerita"
                                if sabor == 2:
                                    sabor = "Portuguesa"
                                if sabor == 3:
                                    sabor = "Moda da Casa"
                                if sabor == 4:
                                    sabor = "Cheddar com Bacon"
                                
                                while True:
                                    print("\nDeseja adicionar bebida? (s/n)")
                                    opcao = input(">")
                                    if opcao == "n" or opcao == "N":
                                        break
                                    if opcao == "s" or opcao == "S":
                                        print("\nQual bebida deseja adcionar?")
                                        print("1- Refrigerante 1L - R$8,00")
                                        print("2- Suco 500ml - R$5,00")
                                        opcao = input(">")
                                        if opcao == "1" or opcao == "2":
                                            break
                                        else:
                                            print("Por favor, selecione uma bebida valida!")
                                    else:
                                        print("Por favor, selecione uma bebida valida!")
                                print("Pedido concluido! Bom Apetite!")
                                pizza = Pizza(sabor, tamanho)
                                pizza.produzir()
                                usuario.adicionarPedido()
                                break
                            else:
                                print("Por favor, selecione um sabor válido.")
                        break       
                           
                    else:
                        print("Selecione um tamanho válido!")
            
            else: 
                print("Já há um pedido em produção!")
        
        if escolha == "2":
            usuario2 = Usuario()
            Usuario.cadastrar(usuario2)

        if escolha == "3":
            if Pizza.producao == True:
                pizza.cancelar()
                print("Pizza foi cancelada!")
            
            if Pizza.producao == False:
                print("Não há nenhuma pizza em produção")
        
        if escolha == "4":
            if usuario.quantidade_pedidos > 0:
                pizza.avaliar()
            else:
                print("Usuário ainda não realizou pedidos nesse incrivel estabelecimento")        

        if escolha == "5":
            print("Obrigado pela preferência. Volte sempre!")
            break

if __name__ == "__main__":
    main()