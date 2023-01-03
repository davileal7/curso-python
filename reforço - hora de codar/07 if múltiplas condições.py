#Usuário pode ou não dirigir

cnh = True
idade_base = 18
idade = int(input('Sua idade: '))

if((cnh == True) and (idade >= 18)):
    print('O usuário pode dirigir um automovel')
else:
    print('Não pode dirigir')