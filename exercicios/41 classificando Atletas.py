from datetime import date
atual = date.today().year
nascimento = int(input("Digite o ano em que o atleta nasceu:"))
idade = atual - nascimento
print("O atleta tem {} anos.".format(idade))
if idade <=9:
    print("O atleta é mirim.")
elif idade <=14:
    print("O atleta é infantil.")
elif idade <=19:
    print("O atleta é junior.")
elif idade <=25:
    print("O atleta é Sênior")


