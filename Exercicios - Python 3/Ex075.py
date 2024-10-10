num = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Mais um valor: ')),
        int(input('O ultimo valor: ')))
print(f'Você digitou o valor {num} ')
print(f'O valor 9 apareceu {num.count(9)} ')
if 3 in num:
        print(f'O valor 3 apareceu {num.index(3)+1}º posição ')
else:
        print(f'O valor 3 não apareceu! ')
print('Os valores pares digitados foram: ', end='')
for n in num:
        if n % 2 == 0:
                print(n, end=' ')
