frase = "curso em video python"
print(frase)
print('Qual a posição da letra (r) na frase ?', frase.index('r') + 1, '° posição')  # end=' ')
print('Quantas letras (v) tem ?', frase.count('v'.upper()))
print('Quantas palavras tem na frase ?', len(frase) - frase.count(' '))
print('A Primeira palavra tem', frase.find(' '), 'letras')
print('Trocando a palavra Python por Git Hub - ', frase.replace('Python', 'Git Hub'))
print('As primeiras palavras em Maiúsculas!', frase.title())
