def aumentar(preço, taxa):
    r = preço + (preço * taxa/100)
    return r

def diminuir(preço, taxa):
    r = preço - (preço * taxa/100)
    return r

def dobro(preço):
    r = preço * 2
    return r

def metade(preço):
    r = preço/2
    return r