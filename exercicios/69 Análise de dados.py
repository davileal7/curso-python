from time import sleep
tot18 = totH = totM20 = 0
while True:
    idade = int(input("Digite sua idade:"))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Digite seu sexo: [M/F]")).strip().upper()
    if idade >= 18:
        tot18 += 1
    if sexo == "M":
        totH += 1
    if sexo == "F" and idade < 20:
        totM20 += 1
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N]")).strip().upper()
    if resp == "N":
         break
sleep(1)
print(f"\033[31mTotal de pessoas com mais de 18 anos:\033[m {tot18}")
print(f"\033[32mAo todo temos {totH} homens cadastrados.\033[m")
print(f"\033[33mE temos {totM20} mulheres com menos de 18 anos.\033[m")
print("Acabou!!!")