media = opc = cont = soma = maior = menor = 0
while opc != 'N':
    n = int(input('Digite um valor: '))
    soma += n
    cont += 1
    media = soma / cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    opc = str(input('Quer continuar? [S/N] ')).upper()
print('A média dos números digitados foi {}'.format(media))
print('O maior valor digitado foi {} e o menor {} '.format(maior, menor))

