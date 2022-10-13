cont = ("zero","um","dois", "trêz", "quatro",
        "cinco","seis","sete","oito","nove",
        "dez", "onze", "doze", "treze", "catorze",
        "quinze", "dezesseis", "dezessete", "dezeito",
        "dezenove","vinte")
while True:
    n = int(input("Digite um número entre 0 e 20: "))
    if 0 <= n <= 20:
        break
    print("Tente novamente. ", end="")
print(f"Você digitou o número {cont[n]}")


