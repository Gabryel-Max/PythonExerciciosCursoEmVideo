print('Digite o valor do produto para saber o preço dele com 5% de desconto')
n = float(input('Digite o valor do produto: '))
d = 0.05 * n
vf = n - d
print('O produto de {} reais ira ficar {:.2f} reais com um desconto de 5%'.format(n, vf))
