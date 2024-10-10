def ficha(nome='<desconhido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato. ')


n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    gols = int(g)
else:
    gols = 0
if n.strip() == '':
    ficha(gols=gols)
else:
    ficha(n, gols)


