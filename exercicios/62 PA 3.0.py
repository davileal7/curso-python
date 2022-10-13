from time import sleep
print("Gerador de PA")
print("-=" * 15)
primeiro = int(input("Digite o primeiro termo:"))
razão = int(input("Digite a razão:"))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} > ".format(termo), end="")
        termo += razão
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais?"))
sleep(3)
print("\033[33mA progressão foi finalizada com {} termos.\033[m".format(total))
print("FIM...")