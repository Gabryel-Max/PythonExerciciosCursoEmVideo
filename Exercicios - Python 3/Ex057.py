sexo = ''
Masculino = ''
Feminino = ''
nome = str(input('Digite seu nome: '))
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print('Sexo invalido, tente novamente!')
if sexo == 'M':
    sexo = 'Masculino'
else:
    sexo = 'Feminino'
print('Nome: {}\nSexo: {} '.format(nome, sexo))

