preço = float(input("Digite o valor da compra:"))
print("""Formas de pagamento
[1] à vista dinheiro/pix (10% desconto).
[2] à vista no débito (5% desconto).
[3] 2x no cartão (preço normal).
[4] 3x ou mais no cartão (+20% juros).""")
opção = int(input("Qual sua opção?"))
if opção == 1:
    total = preço - (preço * 10/100)
elif opção == 2:
    total = preço - (preço * 5/100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print("Sua compra será parcelada em 2x de R$ {}.".format(parcela))
elif opção == 4:
    total = preço + (preço * 20/100)
    totalparcela = int(input("Quantas parcelas?"))
    parcela = total / totalparcela
    print("Sua compra será parcelada em {}x de R$ {} com juros.".format(totalparcela,parcela))
else:
    total = preço
    print("\033[31m Opção inválidada, tente novamente.\033[m")
print("Sua compra de R$ {} vai custar R$ {:.2f} no final.".format(preço,total))


