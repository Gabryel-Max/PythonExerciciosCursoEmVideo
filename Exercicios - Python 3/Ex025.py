nome = str(input('Qual é o seu nome completo?: '))
nome0 = nome.title().split()
nome1 = 'Silva' in nome0
print('Seu nome tem Silva? {} '.format(nome1))
