import math
def soma_hipotenusas(n):
    cateto1 = 1
    cateto2 = n
    i = 1
    j = n
    resultado = 0
    while(i <= n):
        if(cateto1*cateto1 + math.sqrt(cateto2 + cateto2) == n*n):
            resultado += n
        i+=1
        cateto1 +=1
        cateto2 -= 1
        print("#", end="")
    print(resultado)



soma_hipotenusas(25)
