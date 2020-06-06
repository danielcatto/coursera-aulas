print("Fatoral")
#n = int(input("digite um numero inteiro e ZERO para encerrar"))
n =1
while(n != 0):
    n = int(input("digite um numero inteiro e ZERO para encerrar2"))
    i = fat = 1
    while i <= n:
        fat = fat * i
        i = i + 1
    print(fat)
