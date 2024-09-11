import random

def jogar():

    print("Jogo da Forca!")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linhas in arquivo:
        linhas = linhas.strip()
        palavras.append(linhas)
    arquivo.close()

    palavra_misteriosa = palavras[random.randint(0, len(palavras))]
    palavra_escondida = ["_" for letras in palavra_misteriosa]
    letras_erradas = []
    lista_final = [letras for letras in palavra_misteriosa]
    vidas = 6
    pontuacao = 1000



    while True:
        if palavra_escondida == lista_final:
            print("\nPalavra escondida:\n", palavra_escondida)
            print("Parabéns, você acertou!")
            print("Pontuação:", pontuacao, "pontos!")
            break
        
        if vidas == 0:
            print("\nPalavra escondida:\n", lista_final)
            print("Número de vidas: ", vidas)
            print("Letras erradas: ", letras_erradas)
            print("Você perdeu, tente de novo!")
            break

        print("\nPalavra escondida:\n", palavra_escondida)
        print("Número de vidas: ", vidas)
        print("Letras erradas: ", letras_erradas, "\n")
        chute = input(str("Qual seu palpite?\n>"))

        indice = 0
        for letras in palavra_misteriosa:
            if (letras.upper() == chute.upper()):
                palavra_escondida[indice] = letras
            indice = indice + 1
        
        if chute.upper() not in palavra_misteriosa.upper():
            letras_erradas.append(chute.lower())
            vidas = vidas - 1
            pontuacao = pontuacao - 150

    print("\nFim de jogo")



if (__name__ == "__main__"):
    jogar()