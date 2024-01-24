import PySimpleGUI as sg

def get_player(turn):
    if turn %2 == 0:
        return 'x'
    return '0'

coordinates = []
rows = []

for row in range(1, 4):
    column = []
    for col in range(1, 4):
        column.append(sg.Button('  ', key=f'{row}x{col}', font = 'Terminal 20'))
        coordinates.append(f' {row}x{col}')
    rows.append(column)

layout = [
    rows,
]

window = sg.Window('X ir O', layout)
turn = 0
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in coordinates:
        window[event].Update(get_player(turn))

    turn += 1