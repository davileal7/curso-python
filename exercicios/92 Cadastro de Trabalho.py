from datetime import datetime
cadastro = {}
cadastro['Nome'] = str(input('Nome:'))
nasc = int(input('Ano de Nascimento:'))
cadastro['Idade'] = datetime.now().year - nasc
cadastro['CTPS'] = int(input('Carteira de trabalho (0 NÃO tem)'))
if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input('Ano de Contratação:'))
    cadastro['Salário'] = float(input('Salário: R$'))
    cadastro['Aposentadoria'] = cadastro['Idade'] + ((cadastro['Contratação'] + 35) - datetime.now().year)
print('-=-'*30)
for a,b in cadastro.items():
    print(f'- {a} = {b}')
