#Tuplas são imutáveis

lanche = "X Salada", "Hot Dog", "Pizza", "X Bacon", "Batata Frita"
print(sorted(lanche))         #Ordem alfabética
print(lanche)
print(len(lanche))            #Quantas palavras tem em (Lanche)
print(lanche[0], lanche[-1])  #Mostra a primeira palavra e a última.

for palavra in lanche:
   print(f"Eu vou comer {palavra}.")

for ordem in range(0, len(lanche)):
    print(f"\033[32m1) E vou comer {lanche[ordem]} em {ordem+1}°.\033[m")

for posição, quantidade in enumerate(lanche):
    print(f"\033[33m2) Eu vou comer {quantidade} em {posição+1}°.\033[m")

a = (2, 5, 7, 2, 9, 88, 55, 5, 13)
b = (3, 9, 12, 35)
#c = a + b
print(f"{a}\n{b}")       #\n quebra linha
print(len(a))            #QUANTOS caracteres tem?
print(a.count(5))        #CONTA quantos números 5 tem?

#print(b.index(5))
print(a.index(2))        #POSIÇÃO do número 2
if 5 in b:
   print("temos o número 5 no grupo.")
else:
   print("\033[31mNÃO temos o número 5 no grupo.")





