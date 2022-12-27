import requests
import json

cotações = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotações = cotações.json()
cotação_dolar = cotações['USDBRL']['bid']
cotação_euro = cotações['EURBRL']['bid']
#print(cotações)
print('US:', cotação_dolar)
print('EUR:', cotação_euro)