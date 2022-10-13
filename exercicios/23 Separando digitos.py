num = int(input("Informe um número:"))
u = num // 1%10
d = num // 10%10
c = num // 100%10
m = num // 1000%10
print("Analisando o número {}".format(num))
print("Analisando a unidade {}".format(u))
print("Analisando a dezena {}".format(d))
print("Analisando a centena {}".format(c))
print("Analisando o milhar {}".format(m))
