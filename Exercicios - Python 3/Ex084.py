galera = list()
dado = list()
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso (Kg):  ')))
    if len(galera) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    galera.append(dado[:])
    dado.clear()
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp in 'N':
        break
print(f'Você cadastrou {len(galera)} pessoas ')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in galera:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
