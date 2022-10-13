from random import randint
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
computador = randint (0,2)
print("Vamos jogar JO KEN PO!!!")
print("""Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura""")
jogador = int(input("Qual é a sua jogada?"))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
if computador == 0:
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("\033[31mComputador VENCE\033[m")
    else:
        print("Jogada Inválida")
elif computador == 1:
    if jogador == 0:
        print("\033[31mComputador VENCE\033[m")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("Jogador VENCE")
    else:
        print("Jogada INVÁLIDA")
elif computador == 2:
    if jogador == 0:
        print("Jogador VENCE")
    elif jogador == 1:
        print("\033[31mComputador VENCE\033[m")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("Jogada INVÁLIDA")
#print("O computador escolheu {}".format(itens[computador]))
