class Caneca:
    Formato = 'Alça lateral'
    __preço_fabrica = 15     # novo / encapsulamento
    def __init__(self,nome,tamanho,cor):
        self.nome = nome
        self.tamanho = tamanho
        self.cor = cor
        self.status = 'Cheia'
        self.preço = 29.90   # novo


    def beber(self):
        self.status = 'Vazia'
        return f'É da {self.tamanho} que eu estou bebendo '

    def encher(self):
        self.status = 'Cheia'
        return f'Estou echendo a {self.tamanho}'

class Canecalondrina(Caneca):
    def __init__(self):
        super().__init__('nome','tamanho','cor')
        self.bebida = 'Chá'
        self.preço = 20

    def extras(self):
        print('Como brinde, ganhou uma colher!')

    def beber(self):
        self.status = 'Vazia'
        return 'Tá na hora do chá'  # novo

class CanecadoBatman(Caneca):
    def __init__(self):
        super().__init__('nome','Não muito grande','Preto')
        self.bebida = 'café'
        self.preço = 40

    def som(self):
        print('I am Batman!!!')

    def beber(self):
        return super().beber() + f'{self.bebida}'  #novo

caneca_londres = Canecalondrina()
caneca_teste = Caneca('Teste','Menor de todas', 'Branca')
caneca_batman = CanecadoBatman()

print(caneca_teste.beber())
print(caneca_londres.beber())
print(caneca_batman.beber())

print('PROMOÇÃO')
caneca_batman.preço = caneca_batman.preço - 5
caneca_londres.preço = caneca_londres.preço - 5
caneca_teste.preço = caneca_teste.preço - 5

print('NOVO PREÇOS')
print(f'A {caneca_batman.nome} tem o valor de {caneca_batman.preço} reais.')
print(f'A {caneca_teste.nome} tem o valor de {caneca_teste.preço} reais.')
print(f'A {caneca_londres.nome} tem o valor de {caneca_londres.preço} reais.')

print(caneca_teste._Caneca__preço_fabrica)           # 2x __ privado