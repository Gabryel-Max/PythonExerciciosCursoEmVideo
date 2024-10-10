valores = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso! ')
    else:
        print(f'O valor {valor} já se encontra na lista! ')
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'O valores da lista em ordem crescente é {sorted(valores)} ')
