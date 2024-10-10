print('Veja o dobro, triplo e a raiz quadrada de um número')
n = int(input('Digite um número:'))
print('O dobro do número {} é o número {}'.format(n, (n * 2)))
print('O triplo do número {} é o número {}'.format(n, (n * 3)))
print('A raiz quadrada do número {} é o número {:.2f}'.format(n, (pow(n, 1/2))))

