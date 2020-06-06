def maior_elemento(lista):
    num_maior = -10000000
    for i in list(lista):
        if i > num_maior:
            num_maior = i

    return num_maior
lista = [-90, -27, -12]
print(maior_elemento(lista))
