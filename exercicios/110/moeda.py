def aumentar(preço=0, taxa=0, formato = False):
    '''

    :param preço:
    :param taxa:
    :param formato:
    :return:
    '''

    r = preço + (preço * taxa/100)
    return r if formato is False else moeda(r)

def diminuir(preço = 0, taxa = 0, formato = False):
    r = preço - (preço * taxa/100)
    return r if formato is False else moeda(r)

def dobro(preço = 0, formato = False):
    r = preço * 2
    return r if not formato else moeda(r)

def metade(preço = 0, formato = False):
    r = preço / 2
    return r if not formato else moeda(r)

def moeda(preço = 0, moeda ='R$ '):
    return f'{moeda}{preço:>.2f}'.replace('.',',') #replace/troca . por ,

def resumo(preço = 0, juros = 10, desconto = 5):
    print('-' *30)
    print('RESUMO DO VALOR'.center(30))
    print('-' *30)
    print(f'---Preço analisado---: {moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço,True)}')
    print(f'Metade do preço: \t{metade(preço,True)}')
    print(f'{juros}% de aumento: \t{aumentar(preço,juros,True)}')
    print(f'{desconto}% de redução:  \t{diminuir(preço,desconto,True)}')
    print('-' *30)

    #\t = tabulação