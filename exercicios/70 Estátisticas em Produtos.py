total = totmil = menor = cont = 0
barato = 0
while True:
    produto = str(input("Nome do Produto:"))
    preço = float(input("Preço: R$"))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    #else:
     #   if preço < menor:
      #      menor = preço
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if resp == "N":
        break
print("ENCERRADO!!!")
print(f"O total da compra foi R$ {total:.2f}.")
print(f"Temos {totmil} produtos custando mais de R$ 1.000.")
print(f"O produto mais barato custa R${menor:.2f}.")
print(f"O Produto mais barato foi {barato}.")
