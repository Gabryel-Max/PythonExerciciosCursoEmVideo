print('Escreva um número para ver a sua tabuada. ')
n = int(input('Digite um valor: '))
cont = 0
while True:
    cont += 1
    print(f' {n} x {cont} = {n*cont} ')
    if cont == 10:
        n = int(input('Digite um valor: '))
        cont = 0
    if n < 0:
        break
print('Fim... ')