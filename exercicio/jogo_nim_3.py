usuario = 0
computador = 0
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

        
    numPecas = int(input("Informe quantidade de peças para ser retirada: "))
    if(numPecas > m or numPecas <= 0):  
        print("Oops! Jogada inválida! Tente de novo.")
        usuario_escolhe_jogada(n,m)
    else:
        v = numPecas
    return v

def partida():
    global computador
    global usuario

    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print("")
    if(n < m and m > 1):
        print("Oops! Jogada inválida! Tente de novo1.")
        print("")
        vez = True
        partida()
    elif (n % (m+1) == 0):
        print("Você  começa\n")
        vez = True
    elif(n % (m+1) > 0):
        print("O computador começa")
        print()
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
            if(r == 1):
                print("O Usuario tirou uma peça")
            else:
                print("O Usuario tirou " , r , "peças")
            print ("Agora restam ", n , "no tabuleiro.")
            print("")
            if(n <= 0):
                usuario+=1
                print("Fim do jogo! O usuario ganhou!")
                print()
                i=False
                break
            vez = False
            
        elif(vez == False):
            r = computador_escolhe_jogada(n, m)
            n = n - r
            
            if(r == 1):
                print("O computador tirou uma peça")
            else:
                print("O computador tirou " , r , "peças")
            print ("Agora restam ", n , "no tabuleiro.")
            print("")
            
            print("")
            if(n <= 0):
                computador += 1
                print("Fim do jogo! O computador ganhou!")
                print()
                i=False
                break
            vez = True
        else:
            print("Oops! Jogada inválida! Tente de novoELSE.")
            partida()

def campeonato():
    controle = 2
    rodada =1
    while(controle >= 0):
        print("Rodada", rodada)
        controle -= 1
        rodada = rodada + 1
        partida()
        placar()



def placar():
    print("**** Final do campeonato! ****")
    if(usuario < computador ):
        print("computador vence")        
        print("placar você ", usuario, " X ", computador, "computador" )
        print()
    else:
        print("computador vence\n")
        print("placar você ", usuario, " X ", computador, "computador" )
        print()


'''        
print("Bem-vindo ao jogo do NIM! Escolha:")
print(" ")
print("1 - para jogar uma partida isolada ")
tipo_jogo = int(input("2 - para jogar um campeonato "))
print("")

if(tipo_jogo == 1):
    print("voce escolheu partida")
    partida()

elif(tipo_jogo == 2):
    print("voce escolheu campeonato")
    campeonato()
'''



