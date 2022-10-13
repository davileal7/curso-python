print('Tabuada')
n = int(input('Digite um número para saber sua multiplicação até 10: '))
for a in range(1, 10):
    r = n * a
    print(f'\033[;34m{n}\033[m x {a} = {r}')
