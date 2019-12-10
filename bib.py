# Biblioteca de funções que serão utilizadas pelo jogo

#Introdução e regras
def intro():
  print("""Seja bem vindo ao Connect4!

  >> Objetivo do jogo:
      > Posicionar quarto preças iguais de forma adjacente formando uma linha, coluna ou diagonal.
  
  >> Regras:
      > O jogo é composto por 2 jogadores (X ou #) que jogam alternadamente.
      > Cada jogador escolhe uma coluna e a sua peça ocupará a cada mais baixa da mesma.
      > Se ninguém completar o objetivo, será decretado empate.

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

# Validar jogadas (teste de input)




#Michel Moreira - ADS - IFPB CZ - 2019.2
