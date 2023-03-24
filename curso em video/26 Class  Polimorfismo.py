# Possibilidade de rescrever métodos da classe

class Caneca:
    Formato = 'Alça lateral'

    def __init__(self, nome, tamanho, cor):
        self.nome = nome
        self.tamanho = tamanho
        self.cor = cor
        self.status = 'Cheia'

    def beber(self):
        self.status = 'Vazia'
        return f'É da {self.tamanho} que eu estou bebendo '

    def encher(self):
        self.status = 'Cheia'
        return f'Estou echendo a {self.tamanho}'

class Canecalondrina(Caneca):
    def __init__(self):
        super().__init__('nome','tamanho','cor')
        self.bebida = 'Chá'  #Polimorfismo

    def extras(self):
        print('Como brinde, ganhou uma colher!')

    def beber(self):
        self.status = 'Vazia'
        return 'Tá na hora do chá'  #Polimorfismo

class CanecadoBatman(Caneca):
    def __init__(self):
        super().__init__('nome','Não muito grande','Preto')
        self.bebida = 'café'   #Polimorfismo

    def som(self):
        print('I am Batman!!!')

    def beber(self):
        return super().beber() + f'{self.bebida}'  #Polimorfismo

caneca_londres = Canecalondrina()
caneca_teste = Caneca('Teste','Menor de todas', 'Branca')
caneca_batman = CanecadoBatman()

print(caneca_teste.beber())
print(caneca_londres.beber())
print(caneca_batman.beber())
