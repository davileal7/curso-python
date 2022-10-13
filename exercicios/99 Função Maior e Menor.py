from time import sleep

def maior(*núm):
    cont = maior = 0
    print('\nAnalisando os valores passados...')
    print("=" * 30)
    for valor in núm:
        print(f'{valor}', end=" ")
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    sleep(0.5)
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

#Programa Principal
maior(2,9,6,3,4,11)
maior(4,7,0)