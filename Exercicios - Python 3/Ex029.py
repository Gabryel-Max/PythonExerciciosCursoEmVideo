velocidade = float(input('Qual a velocidade atual do carro: '))
multa = (velocidade - 80) * 7
print('-'*64)
if velocidade > 80:
    print('Você foi multado!, o valor a se pagar pela multa é R${:.0f} '.format(multa))
    print('Tenha mais atenção na proxima vez, bom dia!')
else:
    print('Você não foi multado!')
    print('Tenha um bom dia!')
print('-'*64)
