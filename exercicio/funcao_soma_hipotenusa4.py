def eHipotenusa(cateto1, cateto2):
    return ((cateto1*cateto1) + (cateto2*cateto2))
 
def soma_hipotenusas(n):
    h = 1
    soma = 0
    #print("h\t cateto1\tcateto2")
    while (h <= n):
        h_quadrado = (h*h)      
        cateto1 = 1
        cateto2 = 1
        while (cateto1 < n):
            while (cateto2 < n):
                if (h_quadrado == eHipotenusa(cateto1, cateto2)):
                    #print(h,"\t" ,cateto1,"\t",cateto2)
                    soma = soma + h
                    cateto1 = n
                    break
                cateto2 += 1
            cateto1 += 1
            cateto2 = cateto1
        h+= 1
   
    return soma
