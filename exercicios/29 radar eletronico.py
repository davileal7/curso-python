velocidade = float(input("Que velocidade o carro estava?"))
if velocidade >80:
    print("Multado! você excedeu o limite permitido que é 80km/h")
    multa = (velocidade-80) *7
    print("Você deve pagar uma multa no valor de R${} reais".format(multa))
print("tenha um bom dia! dirija com segurança")

