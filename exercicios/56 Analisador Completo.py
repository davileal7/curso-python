somaidade = 0
médiaidade = 0
mih = 0
nv = ""
tm20 = 0
for p in range(1,5):
    print("-----\033[35m{}°PESSOA\033[m-----".format(p))
    nome = str(input("Nome:".format(p)))
    idade = int(input("Idade:".format(p)))
    sexo = str(input("(M/F)".format(p)))
    somaidade += idade
    if p == 1 and sexo == "M":
        mih = idade
        nv = nome
    if sexo in "Mm" and idade > mih:
        mih = idade
        nv = nome
    if sexo in "Ff" and idade < 20:
        tm20 += 1
médiaidade = somaidade / 4
print("A média da idade do grupo é {} anos.".format(médiaidade))
print("O Homem mais velho tem {} anos e se chama {}.".format(mih,nv))
print("Ao todo são {} mulheres com menos de 20 anos.".format(tm20))
