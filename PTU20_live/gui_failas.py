import PySimpleGUI as sg

layout = [
    [sg.Text('Kokas tavo vardas')],
    [sg.Input(key='-INPUT-')],
    [sg.Text(size=(40, 1), key='-OUTPUT-')],
    [sg.Button('Patvirtinti'), sg.Button('Iseiti')],
]

window = sg.Window('Sveiki', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Iseiti':
        break

    window['-OUTPUT-'].update('Sveiki ' + values['-INPUT-'] + ' Nusisypsokit :) ')

text_colour='#a7D060'

window.close()