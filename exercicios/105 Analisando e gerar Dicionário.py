def notas(*n,sit=False):
    """
    >>> Boletim de Notas:
    :param n: uma ou mais notas
    :param sit: avaliação das médias
    :return: dicionário com várias informações
    """
    r = {}
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r["Menor"] = min(n)
    r["Média"] = sum(n)/len(n)
    if sit:
        if r['Média'] >= 7:
            r['Avaliação:'] = 'PARABÉNS'
        elif r["Média"] >= 5:
            r["Avaliação:"] = 'Boa'
        else:
            r['Avaliação:'] = '\033[31mReprovado!'
    return r


resp = notas(10,6.5,9,3.5,sit=True)
print(resp)
help(notas)