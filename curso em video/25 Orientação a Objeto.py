# __init__  - consultor
# self      - acessar métodos e propriedades de uma instância ou métodos

#Objeto
class ControleRemoto:
    def __init__(self,cor,altura,profundidade,largura):  #Caracteristicas
        self.cor = cor
        self.altura = altura
        self.profunfdidade = profundidade
        self.largura = largura

    def passar_canal(self,botao):                       #Métodos
        if botao == '+':
            print('Aumentou o volume')
        elif botao == '-':
            print('Baixou o volume')

    #métodos de controle remoto:
     #   - passar de canal
      #  - mexer no volume
       # - abrir a netflix
        #- desligar Tv

controle_remoto =ControleRemoto('preto','10cm','2cm','2cm')
print(controle_remoto.cor)
controle_remoto.passar_canal('+')