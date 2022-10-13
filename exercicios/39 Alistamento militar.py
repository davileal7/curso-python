from datetime import date
atual = date.today().year
nascimento = int(input("Em que ano você nasceu?"))
idade = atual - nascimento
print("Quem nasceu no ano de {} tem {} anos em {}.".format(nascimento,idade,atual))
if  idade == 18:
    print("Você tem que se alistar imediatamente.")
elif idade < 18:
    saldo = 18 - idade
    print("Ainda faltam {} anos para o seu alistamento.".format(saldo))
    ano = atual + saldo
    print("\033[31mSeu alistamento será em {}.\033[m".format(ano))
elif idade > 18 :
    saldo = idade - 18
    print("Você serviu ou foi já dispensando há {} anos".format(saldo))
    ano = atual - saldo
    print("\033[34mSeu alistamento foi em {}...\033[m".format(ano))
