print('-'*25)
print('Sequência de Fibonacci ')
print('-'*25)
n = int(input('Quantos de termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} - {} '.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' - \033[32m{}\033[m '.format(t3), end='')
    cont = cont + 1
    t1 = t2
    t2 = t3
print('- Fim')
