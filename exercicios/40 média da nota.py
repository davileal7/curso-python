nota1 = float(input("Digite a primeira nota deste bimestre:"))
nota2 = float(input("Digite sua segunda nota do bimestre:"))
média = (nota1 + nota2) /2
print("Tirando a nota {} e {}, a média do aluno é {}".format(nota1,nota2,média))
if média >= 5 and média <7:
    print("\033[31[mCom esta nota o aluno está de recuperação\033[m")
elif média <5:
    print("\033[32mO aluno está reprovado\033[m")
elif média >=7:
    print("\033[34mO aluno está aprovado\033[m")

