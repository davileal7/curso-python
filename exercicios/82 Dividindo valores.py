lista = []
pares = []
impar = []
r = "S"
while r == "S":
    n = int(input("Digite um valor:"))
    lista.append(n)
    r = str(input("Quer continuar? [S/N]")).upper()
    if n %2 == 0:
        pares.append(n)
    else:
        impar.append(n)
print(f"A lista completa é {lista}.")
print(f"Os números pares são {pares}.")
print(f"Os números impares são {impar}.")

#num = []
#pares = []
#impar = []
#while True:
#    num.append(int(input("Digite um número:")))
#    r = str(input("Quer continuar? [S/N]"))
#    if r in "Nn":
#        break
#for i,v in enumerate(num):
#    if v %2==0:
#       pares.append(v)
#    elif v %2==1:
#        impar.append(v)
#print(f"A lista completa é {num}.")
#print(f"Os pares são {pares}.")
#print(f"Os impares são {impar}.")
