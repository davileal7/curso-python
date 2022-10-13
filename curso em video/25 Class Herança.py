class Caneca:
    Formato = 'Alça lateral'

    def __init__(self,tamanho,cor):
        self.tamanho = tamanho
        self.cor = cor
        self.status = 'Cheia'

    def beber(self):
        self.status = 'Vazia'
        return f'É da {self.tamanho} que eu estou bebendo'

    def encher(self):
        self.status = 'Cheia'
        return f'Estou echendo a {self.tamanho}'
#2 Herança
class Canecalondrina(Caneca): # novo
    def __init__(self):
        super().__init__('tamanho','cor')              #Super pega do principal

    def extras(self):
        print('Como brinde, ganhou uma colher!')

class CanecadoBatman(Caneca):
    def __init__(self):
        super().__init__('Não muito grande','Preto')   #Super pega do principal

    def som(self):
        print('I am Batman!!!')



#caneca1 = Canecalondrina()          # novo
#caneca2 = Caneca('Pequena','Roxa')
#caneca3 = Canecalondrina()
#caneca4 = Canecalondrina()
#caneca5 = Canecalondrina()

caneca_londres = Canecalondrina()
caneca_batman = CanecadoBatman()
caneca_londres.extras()
caneca_batman.som()

#print(caneca1.tamanho)
#print(caneca2.tamanho)
#print(caneca3.tamanho)
#print(caneca4.tamanho)
#print(caneca5.tamanho)

#print(caneca1.beber())
#print(caneca2.encher())

#print(caneca1.status)
#print(caneca2.status)

#print(caneca1.Formato)      # novo