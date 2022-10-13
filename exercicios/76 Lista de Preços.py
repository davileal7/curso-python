print(f'\033[34m{"Lista de Materiais e Preços":^40}\033[m')
print("-" *50)
#lista = ("Caderno..................R$ 20.00",
#         "Caneta...................R$ 2.00",
#         "Borracha.................R$ 0.50",
#         "Apontador............... R$ 1.00",
 #        "Livro................... R$ 120.00")
#for a in lista:
#    print(a)
#print("-" *50)

lista = ("Caderno", 19.00,
         "Caneta", 2.00,
         "Impressora", 363.00,
         "Livro", 187.00)
for a in range(0, len(lista)):
    if a % 2 == 0:
        print(f"{lista[a]:.<30}", end="")
    else:
        print(f"R${lista[a]:>7.2f}")
print("-" *50)
