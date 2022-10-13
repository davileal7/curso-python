casa = float(input("Valor da casa? R$"))
sálario = float(input("Qual é o sálario do comprador? R$"))
anos = int(input("Quantos anos de financiamento?"))
prestação = casa / (anos *12)
mínimo = sálario * 30/100
print("Para pagar uma casa de R${} em {}anos".format(casa, anos))
print("a prestação da casa será de R${}".format(prestação))
if prestação <= mínimo:
    print("Empréstimo pode ser CONCEDIDO")
else:
    print("Empréstimo NEGADO")

