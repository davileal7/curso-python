# __init__  - consultor
# self      - acessar métodos e propriedades de uma instância ou métodos

# 1 Abstração
class Caneca:
    def __init__(self, tamanho, cor):
        self.tamanho = tamanho
        self.cor = cor
        self.status = 'Cheia'

    def beber(self):
        self.status = 'Vazia'

    def encher(self):
        self.status = 'Cheia'

caneca1 = Caneca('Grande','Cinza')
caneca2 = Caneca('Pequena','Roxa')

print(caneca1.tamanho)
print(caneca2.cor)

caneca1.beber()
caneca2.encher()

print(caneca1.status)
print(caneca2.status)


class Carro:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

modelo = Carro("Lancer", "Azul")

print(modelo.nome)