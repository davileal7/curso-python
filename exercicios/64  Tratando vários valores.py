soma = 0
cont = 0
n = 0
n = int(input("Digite um número[DIGITE 999 PARA PARAR]:"))
while n != 999:
    soma += n #soma + n
    cont += 1
    n = int(input("Digite um número[DIGITE 999 PARA PARAR]:"))
print("Você digitou {} números e a soma entre eles foi {}".format(cont, soma))
print("FIM...")