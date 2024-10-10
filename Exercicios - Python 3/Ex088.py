import random
from time import sleep

jogos = []

print('=-'*30)
print(f'{"Jogo da MEGA SENA":^60}')
print('=-'*30)
numero_jogos = int(input('Números de jogos: '))

print('=-'*15, 'Jogos', '=-'*15)

for c in range(numero_jogos):
    jogos.append([])
    for i in range(0, 6):
        jogos[c].append(random.randint(1, 60))
    if c != 0:
        sleep(1)
    print(f'Jogo {c+1}: {jogos[c]}')
