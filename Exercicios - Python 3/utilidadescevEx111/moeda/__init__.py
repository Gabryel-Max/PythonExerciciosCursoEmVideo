def metade(p, vof=False):
    metade = p / 2
    return metade if vof is False else moeda(metade)


def dobro(p, vof=False):
    dobro = p * 2
    return dobro if vof is False else moeda(dobro)



def aumentar(valor, taxa, vof=False):
    aumenta = valor + (valor * taxa/100)
    return aumenta if vof is False else moeda(aumenta)


def diminuir(valor, taxa, vof=False):
    diminui = valor - (valor * taxa/100)
    return diminui if vof is False else moeda(diminui)



def moeda(p, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')


def resumo(p, a=0, b=0):
    print('='*30)
    print(f'RESUMO DO VALOR'.center(30))
    print('='*30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'{a}% De Aumento: \t{aumentar(p, a, True)}')
    print(f'{b}% De redução: \t{diminuir(p, b, True)}')

