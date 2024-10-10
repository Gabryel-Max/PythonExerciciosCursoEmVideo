ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1 do aluno: '))
    nota2 = float(input('Nota 2 do aluno: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
print('-'*30)
print(f'{"No":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    print('''[\033[34m999\033[m] INTERROMPE''')
    opc = int(input('Você quer ver a nota de qual aluno? '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de ficha {ficha[opc][0]} são {ficha[opc][1]} ')
print('<<<VOLTE SEMPRE>>>')