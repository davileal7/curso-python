def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor digite um número inteiro\033[m \033[32m(ex:3,45).\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar.\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError,TypeError):
            print('\033[31mERRO! Digite um número real\033[m \033[32m(ex:1.5)\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar!\033[m')
            return 0
        else:
            return n

n1 = leiaInt('Digite um número Inteiro:')
n2 = leiaFloat('Digite um número Real:')
print(f'O número Inteiro foi {n1} e o número Real foi {n2}')
