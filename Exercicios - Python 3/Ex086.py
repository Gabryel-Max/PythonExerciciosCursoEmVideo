'''' num = [[] , [] , []]
num[0].append(int(input('Digite um valor para a posição [0, 0]: ')))
num[0].append(int(input('Digite um valor para a posição [0, 1]: ')))
num[0].append(int(input('Digite um valor para a posição [0, 2]: ')))
num[1].append(int(input('Digite um valor para a posição [1, 0]: ')))
num[1].append(int(input('Digite um valor para a posição [1, 1]: ')))
num[1].append(int(input('Digite um valor para a posição [1, 2]: ')))
num[2].append(int(input('Digite um valor para a posição [2, 0]: ')))
num[2].append(int(input('Digite um valor para a posição [2, 1]: ')))
num[2].append(int(input('Digite um valor para a posição [2, 2]: ')))
print(f'{[num[0][0]]} {[num[0][1]]} {[num[0][2]]}')
print(f'{[num[1][0]]} {[num[1][1]]} {[num[1][2]]}')
print(f'{[num[2][0]]} {[num[2][1]]} {[num[2][2]]}')'''

matriz = [[0,0,0] , [0,0,0] , [0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l] [c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-' *30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()