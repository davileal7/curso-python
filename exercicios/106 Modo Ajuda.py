from time import sleep
c = ('\033[m',      # 0 - sem cor
     '\033[31m',    # 1 - Vermelho
     '\033[32m',    # 2 - Verde
     '\033[33m',    # 3 - Amarelo
     '\033[34m',    # 4 - Azul
     '\033[35m',    # 5 - Roxo
     );

def ajuda(com):
     título(f'Acessando o manual do comando\'{com}\'',4)
     print(c[5],end="")
     help(com)
     print(c[0],end="")
     sleep(2)

def título(msg,cor=0):
     tam = len(msg) +4
     print(c[cor], end="")
     print('=' *tam)
     print(f'  {msg}')
     print("=" *tam)
     print(c[0], end="")
     sleep(1)

comando = ""
while True:
     título('SISTEMA DE AJUDA PyHELP',2)
     comando = str(input("Função ou Biblioteca > "))
     if comando.upper() == "FIM":
          break
     else:
          ajuda(comando)
título('Até Logo',1)

