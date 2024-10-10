from math import hypot
ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))
'''h1 = sqrt((ca**2)+(co**2)'''
h1 = math.hypot(ca,co)
print('A hipotenusa mede: {:.2f}'.format(h1))




