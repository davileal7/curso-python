cont = 0
soma = 0
for n in range(1,11):
    n = int(input("Digite o {}° número:".format(n)))
    if n == 2:
        soma += n
        cont += 1
print("Você informou {} números PARES e a soma foi {}".format(cont,soma))