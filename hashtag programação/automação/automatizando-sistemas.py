import pyautogui
from time import sleep

#clicar na pasta do app
pyautogui.doubleClick(38, 626, duration=2)
#abrir o app
pyautogui.doubleClick(-840, 416, duration=2)


#clicar em cadastrar usuário
pyautogui.click(998, 599, duration=2)
#clicar e digitar nome usuário
pyautogui.click(1016, 542, duration=2)
pyautogui.write('Davi')
#clicar e digitar senha
pyautogui.click(1015, 564, duration=2)
pyautogui.write('123')
#clicar em Registrar novo usuário
pyautogui.click(870, 597, duration=2)

#ENTRAR
pyautogui.click(1016, 542, duration=2)
pyautogui.write('Davi')
#clicar e digitar minha senha
pyautogui.click(1015, 564, duration=2)
pyautogui.write('123')
#clicar em Entrar
pyautogui.click(870, 597, duration=2)


#Extrair cada produto
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        #clicar e digitar produto
        pyautogui.click(726, 531, duration=0.5)
        pyautogui.write(produto)
        #clicar e digitar quantidade
        pyautogui.click(714, 554, duration=0.5)
        pyautogui.write(quantidade)
        #clicar e digitar preço
        pyautogui.click(716, 578, duration=0.5)
        pyautogui.write(preco)
        #clicar em registrar
        pyautogui.click(597, 738, duration=0.5)
        sleep(1)

