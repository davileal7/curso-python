from datetime import date
ano_atual = date.today().year #ano atual
ano_nascimento = int(input("Digite o ano em que o atleta nasceu:"))
idade = ano_atual - ano_nascimento
print("O atleta tem {} anos.".format(idade))
if idade <= 9:
    print("O atleta é mirim.")
elif idade <=14:
    print("O atleta é infantil.")
elif idade <=19:
    print("O atleta é junior.")
elif idade <=25:
    print("O atleta é Sênior")


