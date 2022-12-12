nome = 'Davi'

#Escopo local
if 'nome' in locals():
    print('A váriavel nome esta no escopo local')

if 'idade' in locals():
    print('A váriavel idade esta no escopo local')

#Escopo global
if 'nome' in globals():
    print('A váriavel esta no escopo global')

if 'idade' in globals():
    print('A váriavel idade esta no escopo local')

def teste():
    idade = 18

    if 'idade' in locals():
        print('A váriavel idade esta no escopo local')
    if 'nome' in globals():
        print('A váriavel esta no escopo global')

teste()