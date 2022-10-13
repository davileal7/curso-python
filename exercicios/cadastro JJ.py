def leiapalavra(msg):
    ok = False
    valor = 0
    while True:
        nome = str(input(msg)).strip()
        if nome.isalpha():
            valor = str(nome)
            ok = True
        else:
            print('\033[31mERRO! Digite seu nome apenas com letras (ex: Fábio, Carlos...)\033[m')
        if ok:
            break
    return valor

def frase(texto):
    traço = len(texto)
    print('='*traço)
    print(texto)

resposta = 'S'



frase('Olá tudo bem! seja bem-vindo ao programa de estágio J&J.')
nome = leiapalavra('Digite seu primeiro nome:').strip()
resposta = input(str(f'Prazer {nome}!, vamos começar ou quer corrigir algo? (S/N)')).upper().strip()

if resposta == 'S':
    nome = leiapalavra('Qual é o seu nome?').strip()

input(str('Ok! Conte nos suas conquistas o que marcou sua trajetória?'))

