def cria_matriz(num_linhas, num_colunas,valor):
    '''(int,int,valor) -> matriz (lista de listas)
   Cria e retorn uma matriz com num_linhas e num_colunas
   colunas em que cada elemento e igual ao valor dados.
   '''
    matriz =[] #cria uma matriz vazia
    for i in range(num_linhas):
        #cria a linha i
        linha = [] #lista vazia
        for j in range(num_colunas):
            linha.append(valor)

        #adiciona linha a matriz
            matriz.append(linha)

    return matriz
