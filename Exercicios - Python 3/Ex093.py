jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome do jogador: '))
quantasp = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
for c in range (1, quantasp+1):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
print('='*50)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('='*50)
print(f'O jogador {jogador["Nome"]} jogou {quantasp} partidas. ')
for i, v in enumerate(jogador['Gols']):
    print(f'=>  Na \033[4mpartida\033[m {i+1} fez \033[33m{v}\033[m gols.')
print(f'Foi um total de {jogador["Total"]} gols.')
