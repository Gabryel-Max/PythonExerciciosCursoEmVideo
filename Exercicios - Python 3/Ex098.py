def contador(i, f, p):
    if p < 0:
        p *= 1
    if p == 0:
        p = 1
    print(f'De {i} até {f} pulando de {p} a {p}: ')
    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ')
            cont += p
        print('Fim')
    else:
        cont = i
        while cont >= f:
            print(cont, end=' ')
            cont -= p
        print('Fim')
def lin(a):
    print('-'*a)


lin(25)
contador(1,10, 1)
lin(25)
contador(10, 0, 2)
lin(25)
print('Agora é a sua vez... ')
i = int(input('Digite o início: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
contador(i, f, p)
lin(25)
