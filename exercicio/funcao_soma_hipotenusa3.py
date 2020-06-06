#retorna a soma dos catetos ao quadrado
def eHipotenusa(cateto1, cateto2):
    return ((cateto1*cateto1) + (cateto2*cateto2))
 
def soma_hipotenusas(n):
    #define variaval hipotenusa  que começa valendo um 
    h = 1
    #define variavel soma igual a zero
    soma = 0
    #laço que percorre os valores da hipotenusa de 1 a n
    while (h <= n):
        #define variavel que obtem o valor da hipotenusa a quadrado (h_quadrado) 
        h_quadrado = (h*h)
        #cateto1 e cateto2 começa com 1
        cateto1 = 1
        cateto2 = 1
        #laço que percorre o cateto 1 de ate n que é o limite maximo verdadeiro
        while (cateto1 < n):
            #laço que percorre o cateto2 ate n
            #o laço mais interno vai percorrer de 1 ate n primeiro
            #enquanto o cateto1 estara no valor um, o cateto2 testara de um ate n so depois ira para o proximo valor
            while (cateto2 < n):
                #verifica se o valor da hipotenusa ao quadrado eh igual a soma dos catetos ao quadrado
                if (h_quadrado == eHipotenusa(cateto1, cateto2)):
                    #print(a, " - " ,b , " - " , c)
                    #soma as hipotenusa da condiçao verdadeira do if acima
                    soma = soma + h
                    #iguala o cateto1 ao n do laço para interromper o laço - isso faz que volte para o primeiro laço while para começar testar uma nova hipotenusa
                    cateto1 = n
                 #soma um ao cateto2 para o laço mais interno   
                cateto2 += 1
            
            cateto1 += 1
            cateto2 = cateto1
        h+= 1
   
    return soma
