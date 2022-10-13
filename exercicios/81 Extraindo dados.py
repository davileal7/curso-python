lista = []
while True:
    lista.append(int(input("Digite um valor:")))
    r = str(input("Quer continuar? [S/N]"))
    if r in "Nn":
        break
print(f"Você digitou os valores {len(lista)}")
lista.sort(reverse=True)
print(f"Os valores digitados inversamente são:{lista}")
if 5 in lista:
    print("O número 5 foi digitado.")
else:
    print("O número 5 não foi digitado!!!")
print("ENCERRADO")


