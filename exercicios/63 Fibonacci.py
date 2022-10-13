print("=" * 25)
print("\033[35mSequência de FIBONACCI\033[m")
print("=" * 25)
n = int(input("Quantos termos você quer mostrar?"))
t1 = 0
t2 = 1
t3 = t1 + t2
print("\033[32m{} > {}\033[m ".format(t1,t2), end="")
c = 3
while c <= n:
    t3 = t1 + t2
    print("\033[32m> {} \033[m".format(t3), end="")
    c += 1
    t1 = t2
    t2 = t3
print("FIM...")
