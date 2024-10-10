print('Digite o valor do seu salário para saber quanto ele irá ficar com 15% de aumento')
n = float(input('Digite o valor do salário:'))
ns = n + (n * 15 / 100)
print('O valor do seu salário atual é de {} reais e com um aumento de 15% irá ficar {:.2f} reais '.format(n, ns))

