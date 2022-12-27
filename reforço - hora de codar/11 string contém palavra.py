frase = 'O rato roeu a roupa do rei de Roma'
print(frase)

palavra = 'rato'
palavra2 = 'teste'

if palavra not in frase:
    print('A frase não contém a palavra: ' + palavra)
else:
    print('A frase contém a palavra: '+ palavra)

#2° modo
if frase.count(palavra2) == 0:
    print(f'A frase não contém a palavra: {palavra}')
else:
    print('A frase contém a palavra: ' + palavra)