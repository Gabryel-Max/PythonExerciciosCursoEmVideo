valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
opc = ''
menor = ''
maior = ''
somar = ''
print('''
\033[31m[ 1 ]\033[m SOMAR
\033[32m[ 2 ]\033[m MUTIPLICAR
\033[33m[ 3 ]\033[m MAIOR
\033[34M[ 4 ]\033[m NOVOS NUMEROS
\033[35m[ 5 ]\033[m SAIR DO PROGRAMA''')
while opc != 5:
    opc = int(input('Digite sua opção: '))
    if opc == 1:
        somar = valor1 + valor2
        print('A soma de {} com {} é {} '.format(valor1, valor2, somar))
    if opc == 2:
        multiplicar = valor1 * valor2
        print('A mutiplicação de {} com {} é {} '.format(valor1, valor2, multiplicar))
    if opc == 3:
        if valor2 == valor1:
            print('Valores iguais')
        elif valor1 > valor2:
            maior = valor1
            menor = valor2
        else:
            maior = valor2
            menor = valor1
            print('O valor maior é {} e o menor é {} '.format(maior, menor))
    if opc == 4:
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
else:
    print('Muito obrigado, saindo... ')
