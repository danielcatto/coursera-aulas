import random
def MinMax(temperaturas):
    print("A menor temporatura do mes foi: " ,  minima(temperaturas), "C.")
    print("A maior temporatura do mes foi: " , maxima(temperaturas), "C.")

def minima(temps):
    min = temps[0]
    i = 0
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min

def maxima(temps):
    max = temps[0]
    i = 0
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i = i + 1
    return max

def teste_pontual(temp, valor_esperado):
    valor_calculado = minima(temp)
    if valor_calculado != valor_esperado:
        print("valor errado para array", temp)
        print("valor esperado: ", valor_esperado, "valor calculado: " , valor_calculado)
        print('-----------------------------')

def testa_minimas():
    print("iniciando os testes")
    teste_pontual([0],0)
    teste_pontual([0,0,0,0,0,0], 0)
    teste_pontual([0,1,2,3,4,5,6,7,8,9,10,11],0)
    teste_pontual([30,27,25,26,29,31,32,33,30,29,24,26,30,27,25,25,26,25,22], 22)
    teste_pontual([-15,-12,-5,0,12,15,], -15)

    print("Finalizando os testes")

def testa_maximas():
    print("iniciando os testes")
    temp = []
    for i in range(30):
        t = int(random.uniform(-40, 45))
        temp.append(t)
    teste_pontual(t, 0)
    print("Finalizando os testes")
testa_minimas()
    
