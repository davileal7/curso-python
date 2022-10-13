#while True:
#    for a in range(0,5):
#        int(input("Digite um valor:"))
#        print("Valor adcionado com sucesso!")
#        str(input("Quer continuar [S/N]?"))
números = []
while True:
    n = int(input("Digite um valor:"))
    if n not in números:
        números.append(n)
        print("Valor adcionado com sucesso!")
    else:
        print("Valor duplicado, NÃO ADCIONADO.")
    r = str(input("Quer continuar? [S/N]"))
    if r in "Nn":
        break
print(f"Você adcionou os valores {números}")
print("OBRIGADO")