número = int(input("Digite um número:"))
resultado = (número %2)
if resultado == 0:
    print("\033[33mO número digitado {} é PAR. \033[m".format(número))
else:
    (print("\033[34mO número digitado {} é ÍMPAR. \033[m".format(número)))

