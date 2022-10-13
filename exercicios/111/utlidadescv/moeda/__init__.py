def aumentar(preço=0, taxa=0, formato = False):
    '''
    >> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preço: o preço que se quer reajustar.
    :param taxa: qual é a porcentagem do aumento.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
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
    return f'{moeda}{preço:.2f}'.replace('.',',') #replace/troca . por ,

def resumo(preço = 0, taxaa = 10, taxar = 5):
    print('-' *30)
    print('RESUMO DO VALOR'.center(30))
    print('-' *30)
    print(f'---Preço analisado---: {moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço,True)}')
    print(f'Metade do preço: \t{metade(preço,True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço,taxaa,True)}')
    print(f'{taxar}% de redução:  \t{diminuir(preço,taxar,True)}')
    print('-' *30)