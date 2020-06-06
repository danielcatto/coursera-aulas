#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Exercício-Programa 1 - NIM
def computador_escolhe_jogada(n, m):
    count = m
    deucerto = False
    while (count != 0 and not deucerto):
        if ((n - count) % (m + 1) == 0):
            deucerto = True
        count = count - 1
    count = count + 1
    if (deucerto == False):
        count = m
    countstr = str(count)
    if (count == 1):
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou", countstr, "peças.")
    n = n - count
    if (n != 0):
        print("Agora restam", n, "peças no tabuleiro.")
        print()
        usuario_escolhe_jogada(n, m)
    else:
        print("Fim do jogo! O computador ganhou!")
    return count


def usuario_escolhe_jogada(n, m):
    count = int(input("Quantas peças você vai tirar? "))
    print()
    if (count <= m and count > 0):
        n = n - count
    else:
        print("Oops! Jogada inválida! Tente de novo.")
        print()
        usuario_escolhe_jogada(n, m)
    countstr = str(count)
    if (count == 0):
        print("Voce tirou uma peça.")
    else:
        print("Voce tirou", countstr, "peças.")
    print("Agora resta apenas", n, "peça no tabuleiro.")
    print()
    computador_escolhe_jogada(n, m)
    return count


def partida():
    n = int(input("Quantas peças? "))
    while (n <= 0):
        print("Número de peças inválidas, tente novamente")
        n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print()
    if (n % (m + 1) == 0):
        print("Voce começa!")
        print()
        usuario_escolhe_jogada(n, m)
    else:
        print("Computador começa!")
        print()
        computador_escolhe_jogada(n, m)


def campeonato():
    print()
    print("**** Rodada 1 ****")
    print()
    partida()
    print()
    print("**** Rodada 2 ****")
    print()
    partida()
    print()
    print("**** Rodada 3 ****")
    print()
    partida()
    print()
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você 0 X 3 Computador")


print("Bem-vindo ao jogo do NIM! Escolha:")
print()
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato 2 ")
escolha = int(input())
if (escolha == 1):
    partida()
else:
    campeonato()