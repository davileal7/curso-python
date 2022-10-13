from math import hypot
co = float(input("Comprimento do cateto oposto:"))
ca = float(input("Comprimento do cateto adjacente:"))
hi = hypot(co,ca)
print("A hipotenusda vai medir {:.2f}".format(hi))

