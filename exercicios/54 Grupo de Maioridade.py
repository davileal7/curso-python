from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for p in range(1,8):
    nascimento = int(input("Em que ano a {}° pessoa nasceu?".format(p)))
    idade = atual - nascimento
    if idade >= 18:
        totalmaior += 1
    else:
        totalmenor += 1
print("Ao todo tivemos {} pessoas maiores de idade.".format(totalmaior))
print("Ao todo tivemos {} pessoas menores de idade".format(totalmenor))

