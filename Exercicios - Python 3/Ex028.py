from random import randint
from time import sleep
print('Irei pensar em um número de 1 a 5. Tente adivinhar...')
print('Pensando...')
computador = randint(1, 5)
jogador = int(input('Tente adivinhar: '))
sleep(1)
if computador == jogador:
    print('Você acertou!')
else:
    print('Você perdeu!')
print('O número escolhido foi o {} '.format(computador))



