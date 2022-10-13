n = (int(input("Digite um número:")),
     int(input("Digite outro número:")),
     int(input("Digite mais um número:")),
     int(input("Digite o ultimo número:")))
print(f"Você digitou os valores{n}")
if 5 in n:
    print(f"O valor 5 aparece na: {n.index(5)+1}°posição.")
if 3 in n:
    print(f"O número 3 apareceu: {n.count(3)} vezes.")
else:
    print("O número 3 não foi digitado!")
print(f"Os valores pares foram:", end="")
for n in n:
    if n % 2 == 0:
        print(n)
print("\033[33mFinalizado")


