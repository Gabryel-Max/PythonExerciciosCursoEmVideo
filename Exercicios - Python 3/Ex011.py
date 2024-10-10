print('Digite a altura e a largura da parede para saber quantos litros de tinta sera necessário para pintar . ')
n = float(input('Digite a altura da parede:'))
n2 = float(input('Digite a largura da parede:'))
n3 = float(input('1 litro de tinta pinta quantos metros quadrados?:'))
a = n * n2
l = a / n3
print('Uma parede com {} metros de altura e {} metros de largura gasta {:.1f} litros de tinta. '.format(n, n2, l))


