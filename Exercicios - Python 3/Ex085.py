num = [[] , []]
valor = 0
for c in range(1, 7+1):
    valor = int(input(f'Digie o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=-'*16)
print(f'Os valores pares digitados foram: {sorted(num[0])} ')
print(f'Os valores impares digitados foram: {sorted(num[1])} ')
print('-=-'*16)
