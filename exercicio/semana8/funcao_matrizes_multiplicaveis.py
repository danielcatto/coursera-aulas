def sao_multiplicaveis(m1, m2):
    
    m1y = str(len(m1[0]))
    #print(m1y)
    m2x = str(len(m2))
    #print(m2x)
    if(m1y == m2x):
        return True
    else:
        return False
    
m1  = [[1, 2, 7, 1]]
m2  = [[1, 2, 7, 1], [3, 4, 8, 1],[1, 2, 3, 1],[1, 2, 3, 1],[]]
sao_multiplicaveis(m1,m2)



