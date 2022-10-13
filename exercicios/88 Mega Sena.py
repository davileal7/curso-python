from random import randint
from time import sleep
print("-"*30)
print("       ...MEGA SENA...       ")
print("-"*30)
lista =[]
jogos = []
quant = int(input("Quantos jogos você quer sortear?"))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
print("="*3,f" SORTEANDO {quant} JOGOS","="*3)
for a, l in enumerate(jogos):
    print(f"Jogo {a+1}: {l}")
    sleep(1)
print("="*3,"BOA SORTE","="*3)

