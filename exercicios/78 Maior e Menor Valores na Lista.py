#valores = ["Digite um valor na posição 1:","Digite um valor na posição 2:",
#           "Digite um valor na posição 3:","Digite um valor na posição 4:",
#           "Digite um valor na posição 5:","Digite um valor na posição 6:",
#           "Digite um valor na posição 7:","Digite um valor na posição 8:",
#           "Digite um valor na posição 9:","Digite um valor na posição 10:",]
valores =[]
maior = 0
menor = 0
for a in range(0,6):
    valores.append(int(input(f"Digite um valor para posição {a}:")))
    if a == 0:
        maior = menor = valores[a]
    else:
        if valores[a] > maior:
            maior = valores[a]
        if valores[a] < menor:
            menor = valores[a]
print(f"Você digitou os valores {valores}.")
print(f"O MAIOR valor é {maior} na",end=" ")
for b,c in enumerate(valores):
    if c == maior:
     print(f"{b}° posição.")
print(f"O MENOR valor é {menor} na",end=" ")
for b,c in enumerate(valores):
    if c == menor:
        print(f"{b}º posição.",end=" ")