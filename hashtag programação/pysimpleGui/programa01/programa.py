import PySimpleGUI as sg
from cotacao import pegar_cotacoes

layout = [
    [sg.Text("Pegar Cotação da Moeda")],
    [sg.Text("USD - EUR - GBP - ARS - BTC")],
    [sg.InputText(key="nome_cotacao")],
    [sg.Button("Pegar Cotação"), sg.Button("Cancelar")],
    [sg.Text(key="texto_cotacao")],
]

janela = sg.Window("Sistemas de Cotações", layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        break
    if evento == "Pegar Cotação":
        codigo_cotacao = valores["nome_cotacao"]
        cotacao = pegar_cotacoes(codigo_cotacao)
        janela["texto_cotacao"].update(f"A cotação do {codigo_cotacao} é de {cotacao}")

janela.close()