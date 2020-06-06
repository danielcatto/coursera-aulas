def imprime_matriz(matriz):
    for x in range((len(matriz))):
        for y in range((len(matriz[0]))):
            if (y != len(matriz[0]) - 1):
                print (matriz[x][y], end =" ")
            else:
                print (matriz[x][y])
            
        


