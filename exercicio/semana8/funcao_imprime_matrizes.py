def imprime_matriz(minha_matriz):
    for i in range(len(minha_matriz)):
        for y in range(len(minha_matriz[i])):
            if y == len(minha_matriz[i])-1:
                print(minha_matriz[i][y])
            else:
                print(minha_matriz[i][y],end=" ")
        
minha_matriz = [[1, 2], [3, 4]]
imprime_matriz(minha_matriz)
