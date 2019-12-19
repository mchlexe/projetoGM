# Biblioteca de funções que serão utilizadas pelo jogo

#Introdução e regras
def intro():
  print("""Seja bem vindo ao Connect4!

  >> Objetivo do jogo:
      > Posicionar quarto preças iguais de forma adjacente formando uma linha, coluna ou diagonal.
  
  >> Regras:
      > O jogo é composto por 2 jogadores (✘ ou ✺) que jogam alternadamente.
      > Cada jogador escolhe uma coluna e a sua peça ocupará a cada mais baixa da mesma.
      > Se ninguém completar o objetivo, será decretado empate.
      > Cada jogador pode digitar "FIM" a qualquer momento para desistir.

  >> Bom jogo!
  """)
# Gerar tabuleiro
def tabuleiro():
  espaco = ['◯']
  tabuleiro = []

  for i in range(6):
    linha = []
    for linhas in range(7):
      linha.append(espaco[0])
    tabuleiro.append(linha)
  
  return tabuleiro

# Imprimir tabuleiro
def imprimirTabuleiro(tabuleiro):
  print('1', '2', '3', '4', '5', '6', '7')

  for i in range(6):
    for j in range(7):
      print(tabuleiro[i][j], end=" ")
    print()

# Jogador 1 e Jogador 2

#Executa a jogada chamando as funções Jogador1 e Jogador2
def jogada(tabuleiro, coluna, jogador):
    linhas = 5
    if (jogador == 1):
        tabuleiro = jogador1(tabuleiro,coluna,linhas)
    else:
        tabuleiro = jogador2(tabuleiro,coluna,linhas)

    print(' ')
    imprimirTabuleiro(tabuleiro)

#Executa a jogada do jogador 1.
def jogador1(tabuleiro, coluna, linhas):
    simbolo = ['✘']
    if (tabuleiro[linhas][coluna] == '◯'):
        tabuleiro[linhas][coluna] = simbolo[0]

        return tabuleiro

    else:
        return jogador1(tabuleiro, coluna, (linhas-1))

#Executa a jogada do jogador 2.
def jogador2(tabuleiro, coluna, linhas):
    simbolo = ['✺']

    if (tabuleiro[linhas][coluna] == '◯'):
        tabuleiro[linhas][coluna] = simbolo[0]
        return tabuleiro

    else:
        return jogador2(tabuleiro, coluna, (linhas-1))

# Validar jogadas (teste de input)
def validarJogada(coluna, tabuleiro):
    if((coluna.isdigit() == False) or (int(coluna) > 7) or (int(coluna) < 1)):
        return False

    elif(tabuleiro[0][int(coluna)-1] == '✘' or tabuleiro[0][int(coluna)-1] == '✺'):
        return False

    else:
        return True


#Michel Moreira - ADS - IFPB CZ - 2019.2
