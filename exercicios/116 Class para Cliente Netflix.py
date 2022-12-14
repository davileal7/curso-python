class Cliente:
    def __init__(self,nome,email,plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['basico','premium']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception('Plano Inválido')

    def mudar_plano(self,novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print('Plano Inválido')

    def ver_filme(self,filme,plano_filme):
        if self.plano == plano_filme:
            print(f'Ver filme {filme}')
        elif self.plano == 'premium':
            print(f'Ver filme {filme}')
        elif self.plano == 'basico' and plano_filme == 'premium':
            print('Faça upgrade da sua assinatura.')
        else:
            print('Plano Inválido.')

cliente = Cliente('Davi','davi@hotmail.com','basico')
print(cliente.plano)
cliente.ver_filme('Resident', 'premium')

# no botão upgrade
cliente.mudar_plano('basico')
print(cliente.plano)
cliente.ver_filme('Resident','basico')