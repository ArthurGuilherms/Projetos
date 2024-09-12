import tkinter as tk
from tkinter import messagebox

from contas import Conta
from painel import Painel
from relatorio import Relatorio

aluguel = Conta("Aluguel")
energia = Conta("Energia")
agua = Conta("Agua")
condominio = Conta("Condominio")
internet = Conta("Internet")
iptu = Conta("IPTU")

# Função para centralizar uma janela
def centralizar_janela(janela):
    janela.update_idletasks()
    largura_janela = janela.winfo_width()
    altura_janela = janela.winfo_height()
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    
    x = (largura_tela // 2) - (largura_janela // 2)
    y = (altura_tela // 2) - (altura_janela // 2)
    
    janela.geometry(f'{largura_janela}x{altura_janela}+{x}+{y}')

# Função para abrir a nova janela e inserir valores
def abrir_janela_inserir_valores():
    # Verifica quais opções foram selecionadas
    opcoes_selecionadas = []
    for opcao, var in checkboxes.items():
        if var.get() == 1:
            opcoes_selecionadas.append(opcao)

    if not opcoes_selecionadas:
        messagebox.showwarning("Aviso", "Selecione pelo menos uma conta para calcular.")
        return

    # Cria nova janela para inserir os valores
    janela_valores = tk.Toplevel()
    janela_valores.title("Inserir Valores das Contas")
    janela_valores.geometry('300x250')  # Definindo um tamanho inicial para a janela
    centralizar_janela(janela_valores)  # Centralizando a nova janela

    # Dicionário para armazenar os campos de entrada
    entradas_valores = {}

    # Cria os campos de entrada para as contas selecionadas
    for i, opcao in enumerate(opcoes_selecionadas):
        label = tk.Label(janela_valores, text=f"{opcao}:")
        label.grid(row=i, column=0, padx=10, pady=5)
        entrada = tk.Entry(janela_valores)
        entrada.grid(row=i, column=1, padx=10, pady=5)
        entradas_valores[opcao] = entrada

    # Função para calcular o total
    def calcular_total():
        total = 0
        for opcao, entrada in entradas_valores.items():
            try:
                total += float(entrada.get())
            except ValueError:
                messagebox.showerror("Erro", f"Valor inválido para {opcao}. Insira um número válido.")
                return
        messagebox.showinfo("Total", f"O total das contas selecionadas é: R$ {total:.2f}")

    # Botão para calcular o total
    botao_calcular = tk.Button(janela_valores, text="Calcular Total", command=calcular_total)
    botao_calcular.grid(row=len(opcoes_selecionadas), column=0, columnspan=2, pady=10)

# Criando a janela principal
janela = tk.Tk()
janela.title("Seleção de Contas")
janela.geometry('300x250')  # Definindo o tamanho da janela principal
centralizar_janela(janela)  # Centralizando a janela principal

# Dicionário para armazenar as variáveis das caixas de seleção
checkboxes = {
    "Aluguel": tk.IntVar(value=1),
    "Energia": tk.IntVar(value=1),
    "Água": tk.IntVar(value=1),
    "Condomínio": tk.IntVar(value=1),
    "Internet": tk.IntVar(value=1),
    "IPTU": tk.IntVar(value=0)
}

# Criando as caixas de seleção
for i, (texto, var) in enumerate(checkboxes.items()):
    checkbox = tk.Checkbutton(janela, text=texto, variable=var)
    checkbox.grid(row=i, column=0, padx=10, pady=5)

# Botão para continuar para a próxima etapa
botao_continuar = tk.Button(janela, text="Inserir Valores", command= abrir_janela_inserir_valores)
botao_continuar.grid(row=len(checkboxes), column=0, pady=10)

# Executa a janela
janela.mainloop()
