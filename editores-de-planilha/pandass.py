import pandas as pd

tabela = pd.read_excel('cenprot.xlsx')

#loc indice das linhas
#print(tabela.loc[0:2])---

#indice das linhas e nome das colunas
#print(tabela.loc[0:5, 'Resultado'])---

#iloc: numero das linhas e colunas
tabela_filtro_iloc = tabela.iloc[0:30, 0:2]
#print(tabela_filtro_iloc)---

#print(tabela.filter(['CNPJ', 'Resultado']))---

#FILTRO POR RESULTADO
#print(tabela[tabela['Resultado'] == 'Não Consta'])---
nao_consta = tabela.query("Resultado == 'Não Consta'")
consta = tabela.query("Resultado == 'Consta'")

print(consta)

#nao_consta.to_excel('nova_tabela.xlsx') #to excel para criar