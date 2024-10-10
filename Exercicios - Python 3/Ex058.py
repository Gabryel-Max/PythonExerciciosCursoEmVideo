from random import randint
cont = 0
computador = randint(0, 10)
jogador = ''
print('Irei pensar em um número entre 0 e 10. Tente adivinhar...')
print('-' * 46)
while jogador != computador:
    jogador = int(input('Tente adivinhar: '))
    if jogador == computador:
        cont += 1
        print('Você acertou!')
    else:
        cont += 1
print('O computador escolheu {} '.format(computador))
print('Você acertou depos de {} tentativas '.format(cont))
