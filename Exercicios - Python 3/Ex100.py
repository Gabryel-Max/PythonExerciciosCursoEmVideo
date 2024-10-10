from random import randint
from time import sleep
numeros = list()
def sorteia(b):
    for c in range(0,b):
        numeros.append(randint(1,10))
    print(f'Os valores sorteados foram: {numeros} ')
def somapar():
    somaparr = 0
    print('Lendo valores... ')
    for n in numeros:
        if n % 2 == 0:
            sleep(0.5)
            print(f'\033[32m{n}\033[m ',end=' ')
            somaparr += n
    print(f'<= Valores pares sorteados. ')
    print()
    print(f'O total da soma de todos os valores pares é {somaparr} ')
b = int(input('Quantos valores você quer sortear? '))
sorteia(b)
somapar()
