from datetime import date
atual = date.today().year
nasc = int(input('O ano que você nasceu: '))
idade = atual - nasc
print('A pessoa que nasceu no ano {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que alistar IMEDIATAMENTE!')
elif idade < 18:
    idade = 18 - idade
    ano = atual + idade
    print('O ano que você vai se alistar é {}'.format(ano))
else:
    saldo = idade - 18
    ano = atual - saldo
    print('O ano de seu alistamento foi em {}, FUJA DO \033[31mPAÍS\033[m!'.format(ano))

