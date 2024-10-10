from datetime import date
atual = date.today().year
print('\033[4mColoque seu ano de nascimento para saber qual classe você se encaixa na CNN(Confederação Nacional de Natação).\033[m ')
ano = int(input('Ano de nascimento: '))
idade = atual - ano
print('Você tem {} anos'.format(idade))
if idade <= 9:
    print('Sua classe é \033[1;36mMirim\033[m ')
elif idade <= 14:
    print('Sua classe é \033[1;35mInfantil\033[m ')
elif idade <= 19:
    print('Sua classe é \033[1;33mJunior\033[m ')
elif idade <= 25:
    print('Sua classe é \033[1;30mSênior\033[m ')
else:
    print('Sua classe é \033[4;31mMaster\033[m ')

