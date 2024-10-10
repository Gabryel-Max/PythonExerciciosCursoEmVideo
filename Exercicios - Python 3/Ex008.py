print('Digite um valor em metro para transformar ele em centímetros e milímetros')
n = float(input('Digite um valor em metros: '))
c = n * 100
m = n * 1000
print('O valor de {} metros em centímetros é {:.0f}'.format(n, c))
print('O valor de {} metros em milímetros é {:.0f}'.format(n, m))
