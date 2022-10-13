n = ['casa','branco','verde']
for ordem,lista in enumerate(n): #
    print(f'{ordem+1}° {lista}' ,end=(' '))
print()
lanche = ["X,Salada","Hot Dog","Misto Quente","Coca Cola","Pastel",]
lanche.append("Bacon") #Adcionar
lanche.sort() #Organizar (ordem alfabética)
lanche.sort(reverse=True) #Organiza Inverso
lanche.insert(3,"Calabresa") #Inseri na posição algo
#lanche.pop(1) #Remove o último caracter
#lanche.remove("Misto Quente")
print(len(lanche))
print(lanche)
for d in range(0,4):
    lanche.append(str(input("O que quer acrescentar? ")))
for c,d in enumerate(lanche):
    print(f"No cardapio comprei {d.strip()} que era o {c} da lista")

a = [2,3,4,7]
b = a[:] #CÓPIA
b[2] = 8 #Substituiu o 4 por 8
print(f"Lista A: {a}")
print(f"Lista B: {b}")




