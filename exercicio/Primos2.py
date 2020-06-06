def n_primos(x):
    while(x >=1):
        valor = x
        contar_divisao_inteira = 1
        resto = 0
        mesmo = 0
        i=1
        sim = False
        while(i <= valor):
            resto += valor % i
            if(resto == 0):
                contar_divisao_inteira += 1
            i+=1
        if(contar_divisao_inteira >2):
            return False
        else:
            return True

            fator =2
            while(x >= 2):
                while x % fator != 0 and fator <= x /2:
                    fator = fator + 1
                    if x % fator == 0:
                        print(x, "Nao e primo")
                    else:
                        print(x, "e primo")
                fator=2
                x-=1
        x = x -1

n_primos(10)
