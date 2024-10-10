def voto():
    from datetime import date
    from time import sleep
    atual = date.today().year
    nascimento = int(input('Digite o ano de nascimento: '))
    while True:
        if nascimento > atual:
            print('Ano invalido tente novamente. ')
            nascimento = int(input('Digite o ano de nascimento: '))
        else:
            idade = atual - nascimento
            print(f'Com {idade} anos \033[36m->\033[m ', end='')
            sleep(0.5)
            if 16 <= idade < 18:
                return print('VOTO OPCIONAL', end='')
            elif idade < 16:
                return print('VOTO NEGADO', end='')
            else:
                return print('VOTO OBRIGATORIO', end='')


voto()
