pessoas = []
dados = []
mai = 0
for a in range(0,4):
    dados.append(str(input("Nome:").strip())) #0
    dados.append(int(input("Peso:").strip())) #1
    pessoas.append(dados[:])
    dados.clear()
print(f"As pessoas cadastrasdas foram: {pessoas}, ao todo {len(pessoas)}.")
for b in pessoas:
    if b[1] >=90:
        print(f"{b[0]} está acima de 90 kg, seu peso é: {b[1]} Kg.")
        mai += 1
    else:
        print(f"{b[0]} está abaixo de 90 kg, seu peso é:  {b[1]} Kg.")


pessoas = []
dados = []
mai = men = 0
while True:
    dados.append(str(input("Nome:").strip()))
    dados.append(int(input("Peso:")))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    res = str(input("Quer continuar? [S/N]"))
    if res in "Nn":
        break
print("=" *50)
print(f"Ao todo foram cadastrados {len(pessoas)} pessoas.")
print(f"O MAIOR peso foi de {mai}Kg. Peso de ",end=" ")
for a in pessoas:
    if a[1] == mai:
        print(f"[{a[0]}]",end=" ")
print()
print(f"O MENOR peso foi de {men}Kg. Peso de ",end=" ")
for a in pessoas:
    if a[1] == men:
        print(f"[{a[0]}]",end=" ")
print()








