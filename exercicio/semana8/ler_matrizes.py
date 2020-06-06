def cria_matriz(num_linhas, num_colunas):
    '''(int,int,valor) -> matriz (lista de listas)
   Cria e retorn uma matriz com num_linhas e num_colunas
   colunas em que cada elemento e digitado pelo usuario.
   '''
    matriz =[] #cria uma matriz vazia
    for i in range(num_linhas):
        #cria a linha i
        linha = [] #lista vazia
        for j in range(num_colunas):
            valor = int(input("Digite o elemento ["+str(i)+"]["+str(j)+"] "))
            linha.append(valor)
            print() 
        #adiciona linha a matriz
            matriz.append(linha)
    return matriz


def retorna_matriz():
    for i in matriz:
        print(i, end="\t\n")

def imprime_matriz():
    lin = int(input("Digite o numero de linhas da matriz "))
    col = int(input("Digite o numero de colunas da matriz "))
    return cria_matriz(lin, col)
