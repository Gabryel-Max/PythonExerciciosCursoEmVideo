def fatorial(n, show=False):
    """
     -> Calcula o fatorial do número digitado.
    :param n: O número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: Retorna o valor de n descompactado.
    """
    from math import factorial
    fatorial = factorial(n)
    print(f'O fatorial do número {n}! é {fatorial}')
    if show == True:
        print(f'O calculo fatorial do número {n} é: ')
        for c in range(n, 0, -1):
            print(f'{c}', end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        print(fatorial)
    else:
        print('Calculo OCULTO ')
    return ''


print(fatorial(10, True))
help(fatorial)