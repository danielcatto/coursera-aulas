valor = input("Digite um número inteiro:")
valor_str = str(valor)
tamanho_valor = len(valor_str)
valor_str[tamanho_valor-2]
if(tamanho_valor == 1):
    print("O dígito das dezenas é",0)
else:
    print("O dígito das dezenas é", int(valor_str[tamanho_valor-2]))
