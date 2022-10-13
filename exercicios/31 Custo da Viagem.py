distância = float(input("Digite a distância que você pretente realizar em sua viajem:"))
print("Você esta preste a iniciar sua viagem de {}km/h".format(distância))
if distância <= 200:
    valor = distância * 0.50
else:
    valor = distância * 0.45
print("Sua viagem teve este valor de R${}".format(valor))





