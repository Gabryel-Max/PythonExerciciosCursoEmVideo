numero = int(input('Fatorial do número: '))
resultado = 1
cont = 1
while cont <= numero:
    resultado *= cont
    cont += 1
print('O fatorial de {} é {} '.format(numero, resultado))