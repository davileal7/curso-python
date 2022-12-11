import moeda

valor = float(input('Digite o valor: R$'))
print(f'A metade de R$ {valor} é R$ {moeda.metade(valor)}')
print(f'O dobro de R$ {valor} é R$ {moeda.dobro(valor)}')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(valor, 50)}')
print(f'Com desconto de 25%, temos R$ {moeda.diminuir(valor, 25)}')