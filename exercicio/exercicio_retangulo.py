largura = int(input("Digite a largura do triangulo: "))
altura = int(input("Digite a altura do triangulo: "))
i = 1
alt = 1
while(alt <= altura):
    while(i <= largura):
        print("#", end='')
        i+=1
    alt += 1
    i = 1
    print()
