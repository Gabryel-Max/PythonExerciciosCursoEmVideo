from random import randint
from time import sleep
lista = ["Pedra", "Papel", "Tesoura"]
computador = randint(0, 2)
print('Vamos jogar pedra, papel e tesoura')
print('''escolha alguma dessas opções:
[ 0 ]\033[32mPedra\033[m
[ 1 ]\033[33mPapel\033[m
[ 2 ]\033[34mTesoura\033[m''')
jogador = int(input('Escolha sua jogada: '))
sleep(1)
print('O jogador escolheu {} '.format(lista[jogador]))
print('O computador escolheu {} '.format(lista[computador]))
print('-=-' * 25)
if computador == jogador:
    print('O jogo EMPATOU!')
elif computador == 0 and jogador == 1 or computador == 1 and jogador == 2 or computador == 3 and jogador == 1:
    print('Você VENCEU!')
elif jogador == 0 and computador == 1 or jogador == 1 and computador == 2 or jogador == 3 and computador == 1:
    print('O computador VENCEU!')
print('-=-' * 25)


