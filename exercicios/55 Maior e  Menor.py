maior = 0
menor = 0
for p in range(1,6):
    peso = float(input("Peso da {}° pessoa:".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("\033[31mO maior peso lido foi de {}Kg\033[m".format(maior))
print("\033[32mO menor peso lido foi de {}Kg\033[m".format(menor))

