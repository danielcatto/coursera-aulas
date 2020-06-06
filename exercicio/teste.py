def soma_elementos(x=[]):
    num = 1
    soma = 0
    while num != 0:
        num = int(input('Digite um numero inteiro:'))
        x.append(num)
        # cont = len(x) - 1 # para excluir o ultimo digito
        soma = soma + num
    return soma

soma_elementos()