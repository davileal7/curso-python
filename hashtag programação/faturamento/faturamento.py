import pandas as pd      # pd - apelido

# importar a base de dados
tabela_de_vendas = pd.read_excel('Vendas.xlsx')

# visualizar a base de dados
pd.set_option('display.max_columns', None)
print(tabela_de_vendas)

# faturamento por loja
faturamento = tabela_de_vendas[['ID Loja','Valor Final']].groupby('ID Loja').sum() #filtrar [[ (2x colunas),agrupar as lojas e soma
print(faturamento)

# quandidade de produtos vendidos por loja
quantidade = tabela_de_vendas[['ID Loja','Quantidade']].groupby('ID Loja').sum()
print(quantidade)

print('-'*50)
# ticket médio por produto em cada loja
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
print(ticket_medio)



