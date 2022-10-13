c1 = []
while True:
    c1.append(str(input('Digite seu nome: ').capitalize().strip()))
    print('\033[34mNome cadastrado\033[m')
    r = str(input('Quer continuar? S/N ').upper())
    while r not in 'S''N':
        print('\033[31mERRO!!!\033[m')
        r = str(input('Quer continuar? S/N ').upper())
    if 'N' in r:
        break
print('---Nomes cadastrados---')
for ordem, nomes in enumerate(c1):
    print(f'{ordem + 1}° Nome cadastrado: {nomes}.')
print('FIM')


#def cadastro():
#    while True:
#        c1.append(str(input('Digite seu nome: ').capitalize().strip()))
#        print('\033[34mNome cadastrado\033[m')
#        r = str(input('Quer continuar? S/N ').upper())
#        if r not in 'S''N':
#            print('\033[31mERRO!!!\033[m')
#        if 'N' in r:
#            break
#cadastro()