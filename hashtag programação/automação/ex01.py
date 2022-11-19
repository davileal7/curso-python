from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False) #headless (não mostra o processo)
    pagina = navegador.new_page()
    pagina.goto("https://www.ligamagic.com/?view=home")
    pagina.locator('xpath= //*[@id="mainsearch"]').click()  #atento nos aspas '(fora) "(dentro)
    pagina.fill('xpath= //*[@id="mainsearch"]',"Marcha da Luz de Outro Mundo")
    pagina.locator('xpath= //*[@id="header-mainsearch"]/button[2]/img').click()
    time.sleep(10)

    