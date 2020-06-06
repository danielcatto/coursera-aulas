def soma_elementos(lista):
    resultado = 0

    for i in list(lista):
        resultado += i
    return resultado


lista = [-7,-10,-50,67]
print (soma_elementos(lista))

