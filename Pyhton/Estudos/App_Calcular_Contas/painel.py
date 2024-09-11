from contas import Conta
from relatorio import Relatorio

class Painel:
    lista_pagamentos = []
    numero_cancela = 0
    numero_calcular = 0

    def __init__(self):
        print("\nBem vindo ao calculador de contas!")
        print("Qual conta você deseja calcular?")
        Painel.mostrar_contas()
        Painel.selecionar_contas()
        Painel.calcular_contas()
        Painel.mostrar_divisão()
    
    def mostrar_contas():
        x = 0
        while x != len(Conta.lista_contas):
            print(f'{x + 1} - {Conta.lista_contas[x]}')
            x += 1
        Painel.numero_cancela = x + 1
        print(f'{Painel.numero_cancela} - Apagar lista')
        Painel.numero_calcular = Painel.numero_cancela +1
        print(f'{Painel.numero_calcular} - Calcular')
    
    def selecionar_contas():
        selecao = int(input("\n>"))
        while selecao != Painel.numero_calcular:
            print("\nContas selecionadas:")

            if (selecao - 1) < len(Conta.lista_contas):
                Painel.lista_pagamentos.append(Conta.lista_contas[selecao - 1])

            if selecao == Painel.numero_cancela:
                Painel.apagar_lista

            Painel.mostrar_contas_selecionadas()
            print('')
            Painel.mostrar_contas()
            selecao = int(input("\n>"))
    
    def mostrar_contas_selecionadas():
        nomes_contas = "["
        ultimo_valor = len(Painel.lista_pagamentos) - 1
        for contas_selecionadas in Painel.lista_pagamentos:
            if contas_selecionadas == Painel.lista_pagamentos[ultimo_valor]:
                nomes_contas = nomes_contas + str(contas_selecionadas._nome)
            else:
                nomes_contas = nomes_contas + str(contas_selecionadas._nome) + ", "

        nomes_contas = nomes_contas + "]"
        print(nomes_contas)

    def apagar_lista():
        Painel.lista_pagamentos = []
        nomes_contas = "[]"
    
    def calcular_contas():
        for contas in Painel.lista_pagamentos:
            valor_atribuido = float(input(f'Valor da conta [{contas}] = '))
            contas.informar_valor(valor_atribuido)
            Relatorio.valor_total += valor_atribuido
    
    def mostrar_divisão():
        if (Relatorio._condicao == False):
            for contas in Painel.lista_pagamentos:
                print(f'{contas._nome} = {contas.valor} % {Relatorio._numero} = {contas.valor / Relatorio._numero}')
            print("----------------------------------------")
            print(f'Total = {Relatorio.valor_total} % {Relatorio._numero} = {Relatorio.valor_total / Relatorio._numero}')
        else:
            print("")
            for contas in Painel.lista_pagamentos:
                if contas._nome != "Energia":
                    print(f'{contas._nome} = {contas.valor} % {Relatorio._numero} = {contas.valor / Relatorio._numero}')
                else:
                    print(f'{contas._nome} = {contas.valor}')
            print("----------------------------------------")
            Divisao_total = Relatorio.valor_total / Relatorio._numero
            print(f'Total = {Relatorio.valor_total}')
            print(f'\nHomens = {Divisao_total + (50 / Relatorio._pessoas_condicao)}')
            print(f'Mulheres = {Divisao_total - (50 / (Relatorio._numero - Relatorio._pessoas_condicao))}')
                  


        



