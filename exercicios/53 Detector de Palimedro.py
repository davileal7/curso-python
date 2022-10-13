frase = str(input("Digite uma frase:")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for letra in range(len(junto) -1,-1,-1):
    inverso += junto[letra]
print("O inverso de {} é {}".format(junto,inverso))
if inverso == junto:
    print("\033[32mTemos um palíndromo!\033[m")
else:
    print("\033[31mA frase digitada não é um palíndromo!\033[m")