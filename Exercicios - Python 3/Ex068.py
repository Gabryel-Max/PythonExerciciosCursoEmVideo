from random import randint
computador = randint(0, 10)
jogador = cont = 0
while True:
    jogador = str(input('Sua opção [P = PAR] [I = IMPAR] ')).upper()
    escolha = int(input('Qual o número? '))
    soma = computador + escolha
    resultado = soma % 2
    if jogador == 'P' and resultado == 0:
        cont += 1
        print('Parabens, jogue outra rodada.')
    elif jogador == 'I' and resultado == 1:
        cont += 1
        print('Parabens, jogue outra rodada.')
    elif jogador == 'I' and resultado == 0:
        break
    elif jogador == 'P' and resultado == 1:
        break
print('Você perdeu !')
print(f'O computador escolheu {computador} ')
if resultado == 0:
    print('COMPUTADOR = PAR ')
    print(f'{escolha} + {computador} = {soma}, portanto {soma} é PAR')
else:
    print('COMPUTADOR = IMPAR ')
    print(f'{escolha} + {computador} = {soma}, portanto {soma} é IMPAR')
print(f'{cont} vitórias consecutivas ')
