valores = list()
par = list()
impar = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
    if valor % 2 == 0:
        par.append(valor)
    if valor % 2 == 1:
        impar.append(valor)
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Os valores digitados foram {valores} ')
print(f'Os valores pares digitados foram {par}')
print(f'Os valores impares digitados foram {impar}')
