import pandas as pd

tabela = pd.read_csv('ClientesBanco.csv', encoding='latin1')
tabela = tabela.drop('CLIENTNUM',axis=1)  #remover coluna
print(tabela.info())
print(tabela.describe())
qtde_categoria = tabela['Categoria'].value_counts()
qtde_categoria_perc = tabela['Categoria'].value_counts(normalize=True)
print(qtde_categoria)
print(qtde_categoria_perc)

# Temos várias formas de descobrir o motivo de cancelamento

