from Exercicios.ex115a.lib.interface import *
from Exercicios.ex115a.lib.arquivo import *
from time import sleep

arq = "cursoemvideo.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','EXIT'])
    if resposta == 1:
      # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        print('Saindo do sistema...')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(2)