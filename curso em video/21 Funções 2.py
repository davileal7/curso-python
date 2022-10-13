#help(input) # manual
#print(input.__doc__)

#docstring, manual
def contador(i,f,p):
    """
    Faz uma contagem e mostra na tela.
    :param i: primeiro número
    :param f: último número
    :param p: contagem por número
    :return: sem retorno
    """
    c = 1
    while c <= f:
        print(f'{c}', end=" ")
        c += p
    print("FIM")
contador(0,10,3)
help(contador)

#Parametros Opcinonais
def somar(a,b,c=0):
    s = a+b+c
    print(f'A soma vale {s}.')
somar(3,2,5)
somar(8,7)

# Escopo de Váriavel
# Escopo Local
def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'\033[31mA dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}\033[m')
# Escopo Global
a = 5
teste(a)
print(f'\033[32mA fora vale {a}\033[m')

# Retorno de Valores
def somar(a=0,b=0,c=0): # (r1,r2,r3)
    s = a + b + c
    print(f'A soma vale {s}')
    return s  # irá retornar 3x(a,b,c)

r1 = somar(3,4,5)
r2 = somar(2,2)
r3 = somar(6)
print(f'Os resultados são: {r1}, {r2} e {r3}.')