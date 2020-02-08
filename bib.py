# Biblioteca de funções que serão utilizadas pelo jogo

#Introdução e regras
def intro():
  print("""
                                             |===========================|
                                             |Seja bem vindo ao Connect4!|
                                             |===========================|

|=================||=================||=================||=================||=================||===============|
                                                 【Objetivo do jogo:】                                         
            Posicionar quarto preças iguais de forma adjacente formando uma linha, coluna ou diagonal.
|=================||=================||=================||=================||=================||===============|

|=================||=================||=================||=================||=================||===============|
                                                      【Regras:】                                         
 ➪  O jogo é composto por 2 jogadores (✘ ou ✺) que jogam alternadamente.
 ➪  Cada jogador escolhe uma coluna e a sua peça ocupará a cada mais baixa da mesma.
 ➪  Se ninguém completar o objetivo até as casas acabarem, será decretado empate.
 ➪  Você pode parar o jogo a qualquer momento digitando FIM no lugar onde digita a coluna.
|=================||=================||=================||=================||=================||===============|

                                             |=======================|
                                             |       Bom jogo!       |
                                             |=======================|
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

# Funcoes para verificar o vencedor
# Colunas
def verificaVertical(tabuleiro, jogador):
    linhas = 6
    vertical = []
    colunas = 0

    if(jogador == 1):
        vencedor = "✘✘✘✘"

    elif(jogador == 2):
        vencedor = "✺✺✺✺"

    while(colunas < 7):
        for i in range(linhas):
            vertical.append(tabuleiro[i][colunas])
        vertical = "".join(vertical)

        if(vertical.find(vencedor) != -1):
            return True
        else:
            vertical = list(vertical)
            colunas +=1

    return False

# Linhas
#Linhas horizontais
def verificaHorizontal(tabuleiro, jogador):

    if(jogador == 1):
        vencedor = "✘✘✘✘"

    elif(jogador == 2):
        vencedor = "✺✺✺✺"
    
    for i in range(len(tabuleiro)):
        horizontal = tabuleiro[i]
        horizontal = "".join(horizontal)

        if(horizontal.find(vencedor) != -1):
            return True

    return False

#Michel Moreira - ADS - IFPB CZ - 2019.2