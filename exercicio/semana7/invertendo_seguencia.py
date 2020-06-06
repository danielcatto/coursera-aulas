lista = []
valor = 1
while(valor != 0):
    valor = int(input("Digite um numero: "))
    lista.append(valor)


l = len(lista)-1
while 0 <= l:
    if lista[l] != 0:
        print (lista[l])
    l-=1