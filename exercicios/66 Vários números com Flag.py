s = n = 0
c = s
while True:
    n = int(input("Digite um valor:(\033[34m999 para ENCERRAR\033[m)"))
    if n == 999:
     break
    c += 1
    s += n
print(f"A soma dos {c} valores é = {s}.")
print("Programa finalizado!")
