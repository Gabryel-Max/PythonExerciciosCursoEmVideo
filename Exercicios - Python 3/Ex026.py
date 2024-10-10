frase1 = str(input('Digite uma frase: '))
frase = frase1.lower().strip()
n1 = frase.count('a')
n2 = frase.find('a')
n3 = frase.rfind('a')
print('Quantide de letra "a" aparece: {}'.format(n1))
print('Em que posição ela aparece primeiro: {}'.format(n2))
print('Em que posição ela aparece por ultimo: {}'.format(n3))




