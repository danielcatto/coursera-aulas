def multiplicidade():
    n = int(input("Digite um numero inteiro > 1: "))

    fator = 2
    multiplicidade = 0

    while(n > 1 ):
        while(n % fator == 0):
            multiplicidade += 1
            n = n / fator
        if multiplicidade > 0:
            print("fator ", fator, "multiplicidade = " , multiplicidade)
            numero_primo(multiplicidade)
        fator += 1
        multiplicidade = 0
        
def numero_primo(v):
    valor = v
    contar_divisao_inteira = 1
    resto = 0
    mesmo = 0
    i=1
    sim = False
    while(i <= valor and sim != True):
        resto += valor % i
        if(resto == 0):
            contar_divisao_inteira += 1
        i+=1
    if(contar_divisao_inteira >2):
        print("não primo")
    else:
        print("primo")

multiplicidade()
