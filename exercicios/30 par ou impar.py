número = int(input("Digite um número:"))
resultado = (número % 2)
if resultado == 0:
    print(f"\033[33mO número digitado {número} é PAR. \033[m")
else:
    print(f"\033[34mO número digitado {número} é ÍMPAR. \033[m")

#2° modo
n = 1
par = impar = 0
while n != 0:  # diferente !=
        n = int(input("Digite um valor:"))
        if n % 2 == 0:
                par += 1
        else:
                impar += 1
print(f"Você digitou {par}x números pares e {impar}x impares.")
print("ENCERRADO")