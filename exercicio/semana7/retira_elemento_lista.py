def remove_repetidos(lista):
    num_maior = 0
    lista.sort()
    lista_nova = []
    anterior = -100000000000000
    for i in lista:
        if i != anterior:
            lista_nova.append(i)
            anterior = i
    return lista_nova


lista = [1,1,1,1,2,3,4,4]
remove_repetidos(lista)