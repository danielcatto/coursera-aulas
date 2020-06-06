def soma_matrizes(m1, m2):
    matriz = []
    if (len(m1) == len(m2) and len(m1[0]) == len(m2[0])):
        
        for i in range(len(m1)):
            linha=[]
            for y in range(len(m1[i])):
                linha.append(m1[i][y]+m2[i][y])
            matriz.append(linha)
       
    else:
        return False

    
    return matriz




m1 = [[1,3,4,7],[3,5,6,3],[8]]
m2 = [[8,5,4,4],[2,7,9,7]]
print(soma_matrizes(m1,m2))
