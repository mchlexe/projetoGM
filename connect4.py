# Arquvio main para execução do jogo

import bib
import os

jogar = True
rodadas = 0

#Imprimir regras do jogo
bib.intro()

#Gerar e Imprimir o tabuleiro
tabuleiro = bib.tabuleiro()
bib.imprimirTabuleiro(tabuleiro)

while (jogar == True):
    # Input das jogadas

    print ('\n[Vez do Jogador 1]')
    jogador = 1

    coluna = input("> Informe a coluna que deseja jogar: ")

    while (bib.validarJogada(coluna, tabuleiro) != True):
        if (coluna.upper() == "FIM"):
            # Jogador 1 desistiu, jogador 2 ganha e encerra o jogo.
            print (' ')
            print("✺✺ Jogador 2 ganhou! ✺✺")
            print (' ')
            print("【Jogo encerrado!】")       
            os._exit(1)
                    
        else:
            print ('\n[Vez do Jogador 1]')
            print ("Jogada inválida!")
            coluna = input("➪ Informe a coluna novamente: ")

  
    coluna = int(coluna)
    coluna = coluna - 1

    # Executa jogada
    bib.jogada(tabuleiro, coluna, jogador)

    # Verifica colunas
    if(bib.verificaVertical(tabuleiro,jogador) or bib.verificaHorizontal(tabuleiro,jogador)):
        jogar = False
        print("✘✘ Jogador 1 ganhou! ✘✘")

    if (jogar == True):
        print ('\n[Vez do Jogador 2]')
        jogador = 2

        coluna = input("> Informe a coluna que deseja jogar: ")

        while (bib.validarJogada(coluna, tabuleiro) != True):
                if (coluna.upper() == "FIM"):
                    # Jogador 2 desistiu, jogador 1 ganha e encerra o jogo.
                    print (' ')
                    print("✘✘ Jogador 1 ganhou! ✘✘")
                    print (' ')
                    print("【Jogo encerrado!】")
                    os._exit(1)
                    
                else:
                    print ('\n[Vez do Jogador 2]')
                    print ("Jogada inválida!")
                    coluna = input("➪ Informe a coluna novamente: ")

        
        coluna = int(coluna)
        coluna = coluna - 1

        # Executa jogada
        bib.jogada(tabuleiro, coluna, jogador)

        # Verifica colunas
        if(bib.verificaVertical(tabuleiro,jogador) or bib.verificaHorizontal(tabuleiro,jogador)):
            jogar = False
            print("✺✺ Jogador 2 ganhou! ✺✺")
    
    rodadas += 1

    if(rodadas >= 21):
        jogar = False
        print(' ')
        print('✘✺ Empate! ✺✘')

print (' ')
print("【Jogo encerrado!】")


#Michel Moreira - ADS - IFPB CZ - 2019.2