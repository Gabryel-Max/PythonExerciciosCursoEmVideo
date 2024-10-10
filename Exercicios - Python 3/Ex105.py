def notas(*n, sit=False):
    '''

    :param n: As notas dos alunos
    :param sit: sit=False (Não mostra a situação das notas)
                sit=True (Mostra a situação das notas)
    :return: Retorna (Total de notas registradas, Maior nota, Menor nota e Média das notas)
    '''
    r = dict()
    r['total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'Razoável'
        else:
            r['Situação'] = 'Ruim'
    return r





resp = notas(5.5, 2.5, 8.5,sit=True)
print(resp)


