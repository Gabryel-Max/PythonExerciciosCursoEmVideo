valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'Nn':
        break
print(f'Foram digitados {len(valores)} valores.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente: {valores} ')
if 5 in valores:
    print('O valor 5 foi digitado. ')
else:
    print('O valor 5 não foi digitado. ')
