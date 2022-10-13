# DICIONÁRIO = {} são mutáveis
#             A      B       A          B          A     B
pessoas = {"Nome": "Davi", "Sexo": "Masculino", "Idade": 35}
print(f"{pessoas['Nome']} tem {pessoas['Idade']} anos de idade.")

print(pessoas.keys())    # Nome, Sexo, Idade    - (A)
print(pessoas.values())  # Davi, Masculino, 35  - (B)
print(pessoas.items())   # (Nome:Davi), (Sexo:Masculino), (Idade:35) - (A+B)


# pessoas["Nome"] = "Naara"   # Nome recebe Naara
pessoas['Time'] = 'Corinthians'
del pessoas["Sexo"]  # del - apaga/sexo
pessoas["Peso"] = '84 kg'
print(pessoas)

brasil = []
estado1 = {"Uf": "Rio de Janeiro", "Sigla": "RJ"}   #0
estado2 = {"Uf": "São Paulo", "Sigla": "SP"}        #1
estado3 = {'Estado':'Jacareí'}

brasil.append(estado1)
brasil.append(estado2)
brasil.append(estado3)

print(estado1 , estado3)

estado = {}
brasil = []
for c in range(0, 2):
    estado["Estado"] = str(input("Estado: "))
    estado["Cidade"] = str(input("Cidade: "))
    brasil.append(estado.copy())
for e in brasil:
    for k,v in e.items():
        print(k,v, end=" ")
    print()
