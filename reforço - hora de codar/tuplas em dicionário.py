tuplas = (('Brasil', 'Neymar'), ('Argentina', 'Messi'))
print(tuplas)
print(tuplas[1])

#transformando tupla em dicionário
dicionário = dict((x, y) for x, y in tuplas)
print(dicionário)

print(type(tuplas))
print(type(dicionário))