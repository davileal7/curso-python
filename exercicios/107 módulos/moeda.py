def aumentar(preço, juros):
    r = preço + (preço * juros/100)
    return r

def diminuir(preço, desconto):
    r = preço - (preço * desconto/100)
    return r

def dobro(preço):
    r = preço * 2
    return r

def metade(preço):
    r = preço/2
    return r