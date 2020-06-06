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
    return cont

def usuario_escolhe_jogada(n, m):
    i = True

    if(n<=m or m < 1):
        print("Oops! Jogada inválida! Tente de novo1.")
        print("")
        vez = True
        
    else:

        while(i == True):
            numPecas = int(input("Informe quantidade de peças para ser retirada: "))
            if(n<m or numPecas > m):
                print("Oops! Jogada inválida! Tente de novo.")
                i=True
            elif (numPecas <= 0):
                print("Oops! Jogada inválida! Tente de novo.")
                i=True
            else:
                i=False
        return numPecas


def partida():
    computador = 0
    usuario = 0

    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print("")
    if(n<=m and m > 1):
        print("Oops! Jogada inválida! Tente de novo1.")
        print("")
        vez = True
        partida()
    elif (n % (m+1) == 0):
        print("Você  começa\n")
        vez = True
    elif(n % (m+1) > 0):
        print("O computador começa\n")
        vez = False

    else:
        vez = False
    #ver se jogo é um campeonato(com três rodadas) ou partida única


        #controla a vez de quem joga
    i=True
    while(i):
        if(vez == True):
            r = usuario_escolhe_jogada(n, m)
            n = n - r
            print("O Usuario tirou " , r , "restam " , n)
            print("")
            if(n <= 0):
                usuario+=1
                print("Usuario vence\n")
                print("**** final do compeonato ****")
                print("placar você ", usuario, " X ", computador )
                usuario += 1
                i=False
                break
            vez = False
        elif(vez == False):
            r = computador_escolhe_jogada(n, m)
            n = n - r
            print("O Computador tirou " , r , "restam " , n)
            
            print("")
            if(n <= 0):
                print("computador vence\n")
                print("**** final do compeonato ****")
                print("placar você ", usuario, " X ", computador )
                i=False
                break
            vez = True
        else:
            print("Oops! Jogada inválida! Tente de novoELSE.")
            partida()


print("Bem-vindo ao jogo do NIM! Escolha:")
print(" ")
print("1 - para jogar uma partida isolada ")
tipo_jogo = int(input("2 - para jogar um campeonato "))
print("")

if(tipo_jogo == 1):
    partida()

elif(tipo_jogo == 2):
    controle = 2
    rodada =1
    while(controle >= 0):
        print("Rodada\n", rodada)
        controle -= 1
        rodada = rodada + 1
        partida()


168
