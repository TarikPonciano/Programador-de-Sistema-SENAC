import PySimpleGUI as sg #pip install pysimplegui

sg.theme("DarkAmber")

layout = [[sg.Push(),sg.MLine(key="-ChatBox-", size=(50,10)),sg.Push()],
[sg.Text("Chat: "), sg.Input(key="-InputChat-")],
[sg.Push(),sg.Button("Enviar"),sg.Button("Fechar"),sg.Push()]
]

window = sg.Window("Nova janela", layout)

while True:
    event, values = window.read()

    if event in ('Fechar', sg.WIN_CLOSED):
        break
    if event == "Enviar":
        texto = values["-InputChat-"]
        print(texto)
        window["-InputChat-"].update('')

window.close()