from tkinter import *

'''comando = int(input("\nQual o periodo do pagamento da conta?\n\n1 - Final do mês.  - (Entre os dias 20 e 29)\n"
                "2 - Início do mês. - (Entre o dia 01 e 05)\n3 - Pagamento personalizado.\n\n>> "))
conta = 0
if comando == 1:
    moradores = int(input("\nA conta será dividida pra quantas pessoas?"))
    aluguel = float(input("Quanto foi o aluguel?"))
    condominio = float(input("Quanto foi o condomínio?"))
    agua = float(input("Quanto foi a água?"))
    conta = (aluguel + condominio + agua)
    conta_dividida = conta / moradores
    print("\nA conta deu:\nAluguel:", aluguel, "/", moradores, "=", round(aluguel/moradores, 2), "\nCondomínio:",
          condominio,"/",moradores, '=', round(condominio/moradores, 2), "\nAgua:", agua, "/", moradores, "=",
          round(agua/moradores, 2), "\n----------------------------------------\nTotal =", conta, "/", moradores, "=",
          round(conta_dividida, 2), "para cada.")

if comando == 2:
    moradores = int(input("A conta será dividida pra quantas pessoas?"))
    internet = float(input("Quanto foi a internet?"))
    energia = float(input("Quanto foi a energia?"))
    conta = (energia + internet)
    conta_dividida = conta / moradores
    print("\nA conta deu:\nInternet:", internet, "/", moradores, "=", round(internet / moradores, 2), "\nEnergia:",
          energia, "/", moradores, '=', round(energia / moradores, 2), "\n--------------------------------------"
          "--\nTotal =", conta, "/", moradores, "=", round(conta_dividida, 2), "para cada.")

if comando == 3:
    lista_de_contas = []
    while comando ==3:
        print("\nLista de contas a serem pagas:", lista_de_contas)
        contas = int(input("Adicionar mais alguma?\n1 - Aluguel.\n2 - Condomínio.\n3 - Água.\n4 - Energia.\n5 - "
                       "Internet.\n6 - Refazer a lista de contas a serem pagas.\n7 - Finalizar lista de contas"
                           " e calcular a divisão.\n\n>> "))
        if contas == 1:
            lista_de_contas.append('Aluguel')
        if contas == 2:
            lista_de_contas.append('Condomínio')
        if contas == 3:
            lista_de_contas.append('Água')
        if contas == 4:
            lista_de_contas.append('Energia')
        if contas == 5:
            lista_de_contas.append('Internet')
        if contas == 6:
            lista_de_contas = []
        if contas == 7:
            moradores = int(input("\nA conta será dividida pra quantas pessoas?"))
            relatorio_detalhado = []
            while lista_de_contas != []:
                if "Aluguel" in lista_de_contas:
                    lista_de_contas.remove("Aluguel")
                    aluguel = float(input("Quanto foi o aluguel?"))
                    relatorio = ("Aluguel:", aluguel, "/", moradores, "=", round(aluguel / moradores, 2))
                    relatorio_detalhado.append(relatorio)
                    conta += aluguel
                if "Condomínio" in lista_de_contas:
                    lista_de_contas.remove("Condomínio")
                    condominio = float(input("Quanto foi o condomínio?"))
                    relatorio = "Condomínio:", condominio, "/", moradores, "=", round(condominio / moradores, 2)
                    relatorio_detalhado.append(relatorio)
                    conta += condominio
                if "Água" in lista_de_contas:
                    lista_de_contas.remove("Água")
                    agua = float(input("Quanto foi a água?"))
                    relatorio = "Água:", agua, "/", moradores, "=", round(agua / moradores, 2)
                    relatorio_detalhado.append(relatorio)
                    conta += agua
                if "Energia" in lista_de_contas:
                    lista_de_contas.remove("Energia")
                    energia = float(input("Quanto foi a energia?"))
                    relatorio = "Energia:", energia, "/", moradores, "=", round(energia / moradores, 2)
                    relatorio_detalhado.append(relatorio)
                    conta += energia
                if "Internet" in lista_de_contas:
                    lista_de_contas.remove("Internet")
                    internet = float(input("Quanto foi a internet?"))
                    relatorio = "Internet:", internet, "/", moradores, "=", round(internet / moradores, 2)
                    relatorio_detalhado.append(relatorio)
                    conta += internet
                conta_final = conta / moradores
                comando = 2
                print("\nA conta deu:")
                for i in range(len(relatorio_detalhado)):
                    relatorio_detalhado_new = [str(a) for a in relatorio_detalhado[i]]
                    print(" ".join(relatorio_detalhado_new))
                print("-----------------------------------")
                print("Total: ", conta, "/", moradores, "=", round(conta_final, 2), "para cada.")'''
pessoas = 0
janela = Tk()
janela.title("Calculo de Boletos")

texto_orientacao = Label(janela, text= "Qual o periodo de pagamento da conta?\n" )
texto_orientacao.grid(column=0, row=1)


def verificador_pessoas2():
    pessoas = 2
    return pessoas

def verificador_pessoas3():
    pessoas = 3
    return pessoas

def verificador_pessoas4():
    pessoas = 4
    return pessoas


def numero_pessoas1():
    calculo = 1
    texto_pessoas = Label(janela, text= "\nPara quantas pessoas será dividida a conta?\n")
    texto_pessoas.grid(column=0, row=5)
    botao_pessoas2 = Button(janela, text="2 pessoas", command=verificador_pessoas2)
    botao_pessoas2.grid(column=0, row=6)
    botao_pessoas3 = Button(janela, text="3 pessoas", command=verificador_pessoas3)
    botao_pessoas3.grid(column=0, row=7)
    botao_pessoas4 = Button(janela, text="4 pessoas", command=verificador_pessoas4)
    botao_pessoas4.grid(column=0, row=8)
    return calculo

def numero_pessoas2():
    calculo = 2
    texto_pessoas = Label(janela, text= "\nPara quantas pessoas será dividida a conta?\n")
    texto_pessoas.grid(column=0, row=5)
    botao_pessoas2 = Button(janela, text="2 pessoas", command=verificador_pessoas2)
    botao_pessoas2.grid(column=0, row=6)
    botao_pessoas3 = Button(janela, text="3 pessoas", command=verificador_pessoas3)
    botao_pessoas3.grid(column=0, row=7)
    botao_pessoas4 = Button(janela, text="4 pessoas", command=verificador_pessoas4)
    botao_pessoas4.grid(column=0, row=8)
    return calculo

def numero_pessoas3():
    calculo = 3
    texto_pessoas = Label(janela, text= "\nPara quantas pessoas será dividida a conta?\n")
    texto_pessoas.grid(column=0, row=5)
    botao_pessoas2 = Button(janela, text="2 pessoas", command=verificador_pessoas2)
    botao_pessoas2.grid(column=0, row=6)
    botao_pessoas3 = Button(janela, text="3 pessoas", command=verificador_pessoas3)
    botao_pessoas3.grid(column=0, row=7)
    botao_pessoas4 = Button(janela, text="4 pessoas", command=verificador_pessoas4)
    botao_pessoas4.grid(column=0, row=8)
    return calculo

botao1 = Button(janela, text= "Início do mês.", command=numero_pessoas1)
botao1.grid(column=0, row=2)

botao2 = Button(janela, text= "Fim do mês.", command=numero_pessoas2)
botao2.grid(column=0, row=3)

botao3 = Button(janela, text= "Pagamento personalizado.", command=numero_pessoas3)
botao3.grid(column=0, row=4)

janela.mainloop()