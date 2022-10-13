num = [[],[]]
valor = 0
for a in range(1,8):
    valor=(int(input(f"Digite o {a}° número:")))
    if valor %2==0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f"Os números são: {num}.")
print(f"Os números PARES são: {num[0]}.")
print(f"Os números IMPARES são: {num[1]}.")


