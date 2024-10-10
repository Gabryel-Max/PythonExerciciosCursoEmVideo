primeiro = int(input('Primeiro termo: '))
razao = int(input('A razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(termo, end=' ')
    termo += razao
    cont += 1
print('''
\033[31m[ 0 ]\033[m SAIR DO PROGRAMA''')
opc = ''
while opc == 0:
    opc = int(input('Você quer ver mais quantos termos: '))
    if opc == 0:
        while cont <= opc:
            print(termo, end=' ')
            termo += razao
            cont += 1