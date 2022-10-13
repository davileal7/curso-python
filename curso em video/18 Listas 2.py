#1
#pessoas = []
#dados = []
#dados.append("Pedro")
#dados.append(25,"anos")
#print(dados[0])
#print(dados[1])
#pessoas.append(dados[:])

#pessoas = [("Pedro",25),("Maria", 19),("João",30)]
              #0   #1     #0     #1     #0   #1
                #0            #1          #2
#2
galera = []
dados = []
ma = me = 0
for a in range(0,3):
    dados.append(str(input("Nome:").upper().strip()))
    dados.append(int(input("Idade:")))
    galera.append(dados[:])
    dados.clear()
for g in galera:
    if g[1] >= 18:
        print(f"{g[0]} é maior de idade.")
        ma += 1
    else:
        print(f"{g[0]} é menor de idade.")
        me += 1
print(galera)
print(f"Temos {ma}x que é maior de idade.")
print(f"Temos {me}x que é menor de idade.")



#3
#for p in pessoas:
#    print(f"{p[0]} tem {p[1]} anos de idade.")
    #print(p[0])
#print(pessoas)

#print(pessoas[1][1])
#print(pessoas[2][0])
#print(pessoas[0])
#print(pessoas[1])
#print(pessoas[2])
