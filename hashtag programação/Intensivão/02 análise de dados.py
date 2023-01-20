import pandas

#passo 1
tabela = pandas.read_csv('telecom_users.csv')

#passo 2
tabela = tabela.drop('Unnamed: 0', axis=1)

#passo 3
tabela['TotalGasto'] = pandas.to_numeric(tabela['TotalGasto'], errors='coerce') #trasformando em número
#axix=0-linha, axis=1-coluna
tabela = tabela.dropna(how='all', axis=1)
#linhas que tem pelo menos 1 valor vazio (que possuem algum valor vazio)
tabela = tabela.dropna(how='any', axis=0)
#print(tabela.info())
print(tabela)

#passo 4
