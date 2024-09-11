import advinhacao
import forca

print("Seja bem vindo ao meu jogo!")

escolha = int(input("Qual jogo você deseja jogar?\n1- Advinhação\n2- Forca\n>"))

if escolha == 1:
    advinhacao.jogar()

if escolha == 2:
    forca.jogar()