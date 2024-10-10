while True:
    print('----------CONSOLE PYTHON \033[32mDINOO\033[m--------- ')
    print()
    print('   [ \033[31mFIM\033[m ] PARA ENCERRAR O PROGRAMA ')
    print()
    print('----------CONSOLE PYTHON \033[32mDINOO\033[m---------- ')
    print('Escreva o comando que você esta com dificuldades. ')
    print(f'\033[36m(Lembre-se de escrever o comando corretamente)\033[m ')
    escolha = str(input('Digite o \033[35mcomando\033[m > '))
    if escolha == 'Fim' or escolha == 'fim' or escolha == 'FIM':
        print('\033[31mPrograma encerrado, muito obrigado(a)...\033[m ')
        break
    print('Processando...')
    print('~'*50)
    print(f"Acessando o manual do comando '{escolha}' ")
    print('~'*50)
    print('\033[33m=\033[m' * 90)
    help(escolha)
    print('\033[33m=\033[m'*90)