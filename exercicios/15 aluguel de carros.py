dias = int(input("Qunatos dias alugados:?"))
km = float(input("Qantos km rodados:?"))
pago = (dias*60) + (km*0.15)
print(" O total a pagar é de R${:.2f}".format(pago))
