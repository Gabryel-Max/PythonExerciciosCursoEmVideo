numero = int(input('Digite um número inteiro: '))
print('Escolha a base de conversão:\n[\033[36m 1\033[m ] converter para BINÁRIO\n[\033[31m 2\033[m ] converter para OCTAL\n[\033[33m 3\033[m ] converter para HEXADECIMAL ')
escolha = int(input('Escolha: '))
if escolha == 1:
    binario = bin(numero)
    print('O numéro {} convertido para binário é \033[36m{}\033[m '.format(numero, binario [2:]))
elif escolha == 2:
    octal = oct(numero)
    print('O número {} convertido para octal é \033[31m{}\033[m '.format(numero, octal [2:]))
elif escolha == 3:
    hexa = hex(numero)
    print('O número {} convertido para hexadecimal é \033[33m{}\033[m '.format(numero, hexa [2:]))
else:
    print('Se as opções vai de 1 ate 3 e tu escolheu {} DESCULPA, \033[4;31mMAS TU É UM ANIMAL!\033[m'.format(escolha))
