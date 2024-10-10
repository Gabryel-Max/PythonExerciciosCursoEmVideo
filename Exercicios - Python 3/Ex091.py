from operator import itemgetter
from random import randint
from time import sleep
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
rank = list()
print('Valores sorteados:')
for k, v in jogo.items():
    sleep(1)
    print(f'\033[32m{k}\033[m: tirou \033[35m{v}\033[m no dado.')
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=-'*30)
print('== Ranking dos jogadores ==')
for i, v in enumerate(rank):
    sleep(1)
    print(f'{i+1}º lugar: {v[0]} com \033[33m{v[1]}\033[m no dado.') # {v[0]} == JOGADOR {v[1]} QUANTO ELE TIROU NO DADO
