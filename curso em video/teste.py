def leiaNumero(num):
    ok = False
    valor = 0
    while True:
        numero = str(input(num)).strip()
        if numero.isnumeric():
            valor = int(numero)
            ok = True
        else:
            print('\033[31mERRO! apenas números!!!\033[m')
        if ok:
            break
    return valor

resposta = 'S'


numero = leiaNumero('Digite um número:')
resposta = int(input(f'Você digitou {numero}!, vamos começar ou quer corrigir algo? (S/N)'))


