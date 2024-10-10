matriz = [[0,0,0] , [0,0,0] , [0,0,0]]
total = somacoluna = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l] [c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-' *30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        total += matriz[l] [c]
    print()

print('-'*30)
print(f'A soma de todos os valores é {total} ')
for l in range(0, 3):
    somacoluna += matriz[l][2]
print(f'A soma dos valores da terceira coluna {somacoluna} ')
print(f'O maior valor da segunda linha é {max(matriz[1])} ')
