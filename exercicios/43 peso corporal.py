nome = str(input("Digite seu nome para calcularmos o seu imc:"))
peso = float(input("Qual é o seu peso? (Kg)"))
altura = float(input("Qual é a sua altura? (m)"))
imc = peso / (altura ** 2)
print("O seu IMC {} é de {}".format(nome,imc))
if imc <= 18.5:
    print("Abaixo do peso")
elif imc >=18.5 and imc <25:
    print("Peso ideal")
elif imc >=25 and imc <30:
    print("Sobrepeso")
elif imc >30 and imc <40:
    print("Obesidade")
elif imc >40:
    ("Obesidade máxima")
