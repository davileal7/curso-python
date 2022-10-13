#aluno = {}
#média = []
#aluno = str(input("Digite seu nome:"))
#média = int(input("Qual foi sua nota ?"))
#print(f"A média do aluno{aluno} foi {média}...")
#if média <= 5:
#    print("Reprovado.")
#else:
#    print("Parabéns você foi aprovado!!!")
from time import sleep
aluno = {}
aluno["Nome"] = str(input("Nome: "))
aluno["Média"] = float(input(f"Média de {aluno['Nome']}: "))
if aluno["Média"] <=5:
    aluno["situação"] = "Reprovado"
else:
    aluno["situação"] = "APROVADO!!!"
print("Aguarde!")
sleep(3)
for a,b in aluno.items():
    print(f" - {a}: {b}")
