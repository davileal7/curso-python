import PySimpleGUI as sg

#Criar as janelas e estilos(layout)
def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome')],
        [sg.Input()],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Login', layout=layout,finalize=True)

def janela_pedido():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Fazer Pedido')],
        [sg.Checkbox('Pizza Calabresa', key='pizza1' ),sg.Checkbox('Pizza Bacon',key='pizza2')],
        [sg.Button('Voltar'), sg.Button('Fazer Pedido')]
    ]
    return  sg.Window('Montar Pedido',layout=layout,finalize=True)

#Criar as janelas iniciais
janela1,janela2 = janela_login(), None
while True:
    window,event,values = sg.read_all_windows()
    #Fechar Janela
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break
    if window == janela2 and event == sg.WINDOW_CLOSED:
        break

    #Quando queremos ir para próxima janela
    if window == janela1 and event == 'Continuar':
        janela2 = janela_pedido()
        janela1.hide()
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and event == 'Fazer Pedido':
        if values['pizza1'] == True and values ['pizza2'] == True:
            sg.popup('Foram solicitados uma Pizza de calabresa e Bacon')
        elif values['pizza1'] == True:
            sg.popup('Foi solicitado uma Pizza de calabresa')
        elif values['pizza2'] == True:
            sg.popup('Foi solicitado uma Pizza de Bacon')

