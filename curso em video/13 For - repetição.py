# FOR(repete) IN(dentro)

#1° método
for contar in range(0,3):
    print('teste')

for numeros in range(0, 20, 3): # i,f,p
    print(numeros)


#2° método

carros = ['Celta', 'Gol']  # CARROS uma lista com 2 objetos.
carros2 = []
print('Temos 2 carros em uma lista e queremos adcionar mais 3!')
for ordem, lista in enumerate(carros):
    print(f'O {ordem+1}° carro da lista é {lista}.')
for pergunta in range(1, 2):
    carros2.append(input(str('Qual carro quer acrecentar? ')).strip())
for ordem, lista2 in enumerate(carros2):
        print(f'E foi adicionado {lista2} na {ordem+3}° posição da lista.')
print()

#3° método
for a in range(0, 11, 2):
    print(a, end=" ")
print()
print('A lógica foi de 2 em 2 até 10.')
print("FIM")





