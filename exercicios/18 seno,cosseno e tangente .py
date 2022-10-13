from math import radians,sin,cos,tan
ângulo = float(input("Digite o angulo para ver o valor do seno e cosseno e tangente:"))
seno = sin(radians(ângulo))
print("o Angulo de {} tem o SENO de {:.2f}".format(ângulo,seno))
cosseno = cos(radians(ângulo))
print("O angulo de {} tem o COSSENO de {:.2f}".format(ângulo,cosseno))
tangente = tan(radians(ângulo))
print("O angulo de {} tem a TANGENTE de {:.2f}".format(ângulo,tangente))

