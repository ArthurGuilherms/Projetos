from pizza import Pizza
from usuario import Usuario
from bebida import Bebida

class Sistema:
    def __init__(self):
        # Inicializa o sistema com variáveis para login, lista de usuários, pedidos e opiniões
        self.login = False
        self.usuarios = []
        self.pedidos = []
        self.opinioes = []

def main():
    # Cria uma instância do sistema e do usuário
    sistema = Sistema()
    usuario = Usuario()
    
    print("Bem vindo ao menu!")

    # Loop principal do sistema
    while True:
        # Se o usuário não estiver logado, chama o método de login
        if usuario.login == False:
            Usuario.logar(usuario)
        # Se o usuário estiver logado, exibe o menu de opções
        if usuario.login == True:
            print("1- Fazer Pedido")
            print("2- Cancelar Pedido")
            print("3- Opinar")
            print("4- Sair")
            escolha = input("\nEscolha uma opção: ")

            # Opção 1: Fazer pedido de pizza
            if escolha == "1":
                # Verifica se já existe uma pizza em produção
                if Pizza.producao == False:
                    while True:
                        # Seleciona o tamanho da pizza
                        print("\nQual o tamanho da pizza? (P/M/G)")
                        print("P = R$22,99")
                        print("M = R$25,99")
                        print("G = R$29,99")
                        tamanho = input("\n>")
                        if tamanho in ["P", "p", "M", "m", "G", "g"]:
                            while True:
                                # Seleciona o sabor da pizza
                                print("\nQual sabor desejado?")
                                print("1- Marguerita")
                                print("2- Portuguesa")
                                print("3- Moda da Casa")
                                print("4- Cheddar com Bacon")
                                sabor = input("\n>")
                                print(sabor)
                                if sabor in ["1", "2", "3", "4"]:
                                    # Define o sabor da pizza baseado na escolha do usuário
                                    if sabor == "1":
                                        sabor = "Marguerita"
                                    elif sabor == "2":
                                        sabor = "Portuguesa"
                                    elif sabor == "3":
                                        sabor = "Moda da Casa"
                                    elif sabor == "4":
                                        sabor = "Cheddar com Bacon"
                                    
                                    # Pergunta se o usuário deseja adicionar uma bebida
                                    while True:
                                        print("\nDeseja adicionar bebida? (s/n)")
                                        opcao = input(">")
                                        if opcao in ["n", "N"]:
                                            break
                                        if opcao in ["s", "S"]:
                                            print("\nQual bebida deseja adcionar?")
                                            print("1- Refrigerante 1L - R$8,00")
                                            print("2- Suco 500ml - R$5,00")
                                            opcao = input(">")
                                            if opcao in ["1", "2"]:
                                                break
                                            else:
                                                print("Por favor, selecione uma bebida valida!")
                                        else:
                                            print("Por favor, selecione uma bebida valida!")
                                    print("Pedido concluído! Bom Apetite!")
                                    
                                    # Cria a pizza, inicia a produção e adiciona o pedido ao usuário
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
            
            # Opção 2: Cancelar pedido
            if escolha == "2":
                if Pizza.producao == True:
                    pizza.cancelar()
                    print("Pizza foi cancelada!")
                else:
                    print("Não há nenhuma pizza em produção")
            
            # Opção 3: Avaliar o pedido
            if escolha == "3":
                if usuario.quantidade_pedidos > 0:
                    pizza.avaliar()
                else:
                    print("Usuário ainda não realizou pedidos nesse incrível estabelecimento")        

            # Opção 4: Sair do sistema
            if escolha == "4":
                print("Obrigado pela preferência. Volte sempre!")
                break

if __name__ == "__main__":
    main()