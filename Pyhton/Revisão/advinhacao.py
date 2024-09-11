import random

def jogar():
    print("Jogo de advinhação!")

    numero_secreto = random.randint(1,101)
    numero_tentativas = 0
    pontos = 0

    print("\nQual o nível de dificuldade?")
    print("1 -Fácil | 2- Médio | 3- Difícil\n ")

    nivel = int(input(">"))

    if (nivel == 1):
        numero_tentativas = 10
        pontos = 1000
        print("Nível Fácil")

    elif (nivel == 2):
        numero_tentativas = 6
        pontos = 2000
        print("Nível Médio")

    elif (nivel == 3):
        numero_tentativas = 4
        pontos = 3000
        print("Nível Difícil")

    pontos_totais = pontos

    for rodada in range(1, numero_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, numero_tentativas))
        chute_str = input("Escolha um número entre 1 e 100\n> ")
        chute = int(chute_str)

        if (chute <= 1 or chute >= 100):
            print("Número Inválido, perdeu uma chance")
            continue

        maior = chute > numero_secreto
        menor = chute < numero_secreto
        igual = chute == numero_secreto

        if (maior):
            print("O número escolhido é maior que o secreto\n")

        elif (menor):
            print('Número escolhido é menor que o número secreto\n')

        elif(igual):
            print("Você acertou!\n")
            print("Pontuação: {}".format(round(pontos)))
            break

        pontos = pontos - (pontos_totais / numero_tentativas)

    print("O número escolhido era {}".format(numero_secreto))
    print("Fim do Jogo")

if (__name__ == "__main__"):
    jogar()
