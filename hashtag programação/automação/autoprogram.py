from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False) #headless (não mostra o processo)
    pagina = navegador.new_page()
    pagina.goto("https://www.google.com.br/")
    pagina.locator('xpath= /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').click()  #atento nos aspas '(fora) "(dentro)
    pagina.fill('xpath= /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input',"playwright python")
    pagina.locator('xpath= /html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
    pagina.locator('xpath= //*[@id="rso"]/div[1]/div/div/div/div[2]/ul/li/div/div/div/div[1]/div/a/h3').click()
    time.sleep(10)