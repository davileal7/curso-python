from random import randint
from time import sleep
from operator import itemgetter
jogo = {'\033[31mjogador 1\033[m': randint(1,6),
        '\033[32mjogador 2\033[m': randint(1,6),
        '\033[33mjogador 3\033[m': randint(1,6),
        '\033[34mjogador 4\033[m': randint(1,6)}
print('Valores sorteados')
for a,b in jogo.items():
        print(f'{a} tirou {b} no dado.')
        sleep(1)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=-'*30)
print('== Ranking dos Jogadores ==')
for a,b in enumerate(rank):
        print(f' {a+1}° lugar: {b[0]} com {b[1]}.')
        sleep(1)