time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    quantasp = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
    partidas.clear()
    for c in range (1, quantasp+1):
        partidas.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print('='*50)
print('cod', end =' ')
for i in jogador.keys():
    print(f'{i:<15} ',end='')
print()
print('='*50)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('='*50)
while True:
    busca = int(input('Mostrar dados de qual jogar?(999 interrompe): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe o jogador com o código {busca} ')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'  No jogo {i+1} fez {g} gols.')
    print('='*50)
print('Volte sempre! ')
