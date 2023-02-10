import PySimpleGUI as sg #pip install pysimplegui

sg.theme("DarkAmber")

layout = [[sg.Text("Teste")],
[sg.Button("Fechar")]
]

window = sg.Window("Nova janela", layout)

while True:
    event, values = window.read()

    if event in ('Fechar', sg.WIN_CLOSED):
        break

window.close()