def notas(*n, sit=False):
    '''

    :param n: digite as notas
    :param sit: opcional, retorna a situação
    :return: um dicionário com total, maior, menor, média e situação
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média']>=7:
            r['situação'] = 'boa'
        if r['média'] >=5:
            r['situação'] = 'razoável'
        else:
            r['situação'] = 'ruim'
    return r



print(notas(5, 6, 2, 6, sit=True))
help(notas)

