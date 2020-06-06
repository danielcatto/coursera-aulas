def retangulo(x,y):

    largura = x #int(input("Digite a largura do triangulo: "))
    altura = y #int(input("Digite a altura do triangulo: "))
    i = 1
    alt = 1
    while(alt <= altura):
        while(i <= largura):
            if(alt == 1 or alt == altura): 
                print("#", end='')
            elif(i==1 or i == largura):
                print("#", end='')
            else:
                print(" ",end="")
            i+=1
        alt += 1
        i = 1
        print()


retangulo(30,10)
