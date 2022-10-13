sálario = float(input("Qual é o sálario do funcionário?"))
if sálario <= 1250:
    novo = sálario + (sálario * 15/100)
else:
    novo = sálario + (sálario * 10/100)
print("Quem ganhava R${} passa a ganhar R${}".format(sálario,novo))
