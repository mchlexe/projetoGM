# Arquvio main para execução do jogo

import bib
import os

jogar = True
# rodadas = 0

#Imprimir regras do jogo
bib.intro()

#Gerar e Imprimir o tabuleiro
tabuleiro = bib.tabuleiro()
bib.imprimirTabuleiro(tabuleiro)

while (jogar == True):
  #Input das jogadas
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
          print (' ')
          print ("Jogada inválida!")
          coluna = input("➪ Informe a coluna novamente: ")

  
  coluna = int(coluna)
  coluna = coluna - 1

  bib.jogada(tabuleiro, coluna, jogador)

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
                print (' ')
                print ("Jogada inválida!")
                coluna = input("➪ Informe a coluna novamente: ")

  
  coluna = int(coluna)
  coluna = coluna - 1

  bib.jogada(tabuleiro, coluna, jogador)
  
#   rodadas += 1
# #Como encerrar o jogo (Ganhando ou por pedido do usuário)
#   if (rodadas >= 21):
#     jogar = False
#     print(' ')
#     print('✘✺ Empate! ✺✘')


#Michel Moreira - ADS - IFPB CZ - 2019.2
