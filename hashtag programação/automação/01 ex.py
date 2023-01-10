from playwright.sync_api import sync_playwright
import time

#acessa google tradutor
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) #headless (não mostra o processo)
    page = browser.new_page()
    page.goto("https://translate.google.com.br/?sl=pt&tl=en&text=Obrigado&op=translate&hl=pt-BR")
    time.sleep(2)
    page.locator('xpath= //*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/div[1]').click() #limpa a tela
    time.sleep(2)
    page.fill('xpath= //*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea','Olá, Mundo.') #escreve
    time.sleep(2)
    page.locator('xpath= //*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/div[1]').click() #limpa a tela
    time.sleep(2)
    page.fill('xpath= //*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea','Programa de Automatização.')
    time.sleep(10)

    # page.screenshot(path="example02.png")