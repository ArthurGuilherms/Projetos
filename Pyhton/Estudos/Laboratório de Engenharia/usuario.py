class Usuario:
    lista_usuarios = []
    lista_senhas = []

    def __init__(self):
        self.nome = ""
        self.endereco = "" 
        self.telefone  = ""
        self.senha = ""
        self.login = False
        self.quantidade_pedidos = 0

    def cadastrar(self):
        self.nome = input("\nNome:")
        Usuario.lista_usuarios.append(self.nome)
        self.endereco = input("Endereço:")
        self.telefone = input("Telefone:")
        self.senha = input("Senha:")
        Usuario.lista_senhas.append(self.senha)
        self.login = False
        print("Usuario adicionado com sucesso!\n")
       
    def logar(self):
        if self.login == True:
            print("Usuário já está logado")
        if self.login == False:
            while True:
                print("\n1- Registrar")
                print("2- Login")

                selecao = input("\nEscolha uma opção:")
                if selecao == "1":
                    Usuario.cadastrar(self)
                    break

                if selecao == "2":
                    verificaNome = input("Nome:")
                    if (self.nome == verificaNome):
                        verificaSenha = input("Senha:")
                        if (self.senha == verificaSenha):
                            self.login = True  
                            print("Login realizado!\n")
                            break
                        else:
                            print("Senha incorreta")

                    else:
                        print("Usuário não encontrado!")


    def adicionarPedido(self):
        self.quantidade_pedidos += 1