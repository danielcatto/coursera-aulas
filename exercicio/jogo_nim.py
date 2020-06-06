#!/usr/bin/python
# -*- coding: UTF-8 -*-
computador = 0
usuario = 0
def computador_escolhe_jogada(n , m):
    loop = True
    cont = m
    if(n == m):
        return m
    elif(n - m == 1):
        return m
    else:
        while(loop):
            if(((n - cont ) % (m+1))== 0):
                loop = False
            cont = cont  - 1
    cont = cont + 1
    if(cont<= 0):
        cont=m
    n = n - cont
    print("Voce tirou", cont, "peças.")
    print("Agora resta apenas", n, "peça no tabuleiro.")
    return cont

def usuario_escolhe_jogada(n, m):
    i = True
    numPecas = int(input("Quantas peças você vai tirar?"))
    while(i == True):
        if (numPecas <= m ):
            i=False
            return numPecas
        elif(numPecas > m and numPecas <= m):
            print("Oops! Jogada inválida! Tente de novo.")
            numPecas = int(input("\nQuantas peças você vai tirar? "))
            i=False
    print("Voce tirou", numPecas, "peças.")
    print("Agora resta apenas", n, "peça no tabuleiro.")
    return numPecas

def  partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if(n < m or  m == n):
        print("Oops! Jogada inválida! Tente de novo")
        partida()
    else:
        if (n % (m+1) == 0):
            print("\nVoce começa! \n")
            vez = True
        elif(n % (m+1) != 0):
            print("false")
            vez = False
        else:
            vez = False
    #ver se jogo é um campeonato(com três rodadas) ou partida única
    #controla a vez de quem joga
    i=True
    while(i):
        if(vez == True):
            usuario_escolhe_jogada(n, m)
            if(n <= 0):
                print("Usuario vence")
                i=False
            vez = False
        elif(vez == False):
            computador_escolhe_jogada(n, m)

            if(n <= 0):
                print("computador vence")
                i=False
            vez = True

def campeonato():
    print()
    rodada = 1
    while(rodada <= 3):
        print("**** Rodada %i ****" % rodada)
        partida()
        rodada += 1



print("Bem-vindo ao jogo do NIM! Escolha:")
print(" ")
print("1 - para jogar uma partida isolada ")
tipo_jogo = int(input("2 - para jogar um campeonato "))
print(" ")

if(tipo_jogo == 1):

    partida()
elif(tipo_jogo == 2):
    controle = True
    rodada =1
    while(controle):
        campeonato()
        controle -= 1
        if(rodada == 3):
            controle = False
    rodada = rodada + 1
    print("**** final do compeonato ****")
    print("placar você ", usuario, " X ", computador )


