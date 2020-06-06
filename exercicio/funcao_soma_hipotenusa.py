import math

def eHipotenusa(cateto1 , cateto2):
    return ((cateto1*cateto1) + (cateto2*cateto2))

def soma_hipotenusas(n):
    cateto1=1
    cateto2=1
    i = 1
    soma = 0
    while(i <= n):
        n2 = n*n
        while(cateto1 < n):
            while(cateto2 < n):
                if(n2 == eHipotenusa(cateto1,cateto2)):
                    print(cateto1 ," + ", cateto2)
                    soma+=n
                    cateto1=n
                    break
                cateto2 += 1
            cateto1+= 1
        i+=1
    return soma


    


    
print(soma_hipotenusas(25))
