import math
g = float(input('Digite o valor em grau: '))
ar = math.radians(g)
seno = math.sin(ar)
cos = math.cos(ar)
tan = math.tan(ar)
print('-'*71)
print('Um triângulo retângulo com grau de {:.0f}° tem seno, cos e tan no valor de:\nCosseno: {:.2f}\nSeno: {:.2f}\nTangente: {:.2f}'.format(g,seno, cos, tan))
print('-'*71)