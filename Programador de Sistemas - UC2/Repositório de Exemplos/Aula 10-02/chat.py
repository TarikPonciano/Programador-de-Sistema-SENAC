import PySimpleGUI as sg #pip install pysimplegui

sg.theme("DarkAmber")

tela1 = [[sg.Text("Escolha seu nome: "), sg.Input(key="-NomeInput-")],
[sg.Button("Entrar"), sg.Button("Fechar")]]

tela2 = [[sg.Push(),sg.MLine(key="-ChatBox-", size=(50,10)),sg.Push()],
[sg.Text("Chat: "), sg.Input(key="-InputChat-")],
[sg.Push(),sg.Button("Enviar"),sg.Button("Voltar",key="-VoltarChat-"),sg.Push()]
]

layout = [[sg.Column(tela1, key="-Tela1-", visible=True), sg.Column(tela2, key="-Tela2-", visible = False)]]

chatLog = ''''''
usuario = ""
window = sg.Window("Chat Simples", layout)

while True:
    event, values = window.read()

    if event in ('Fechar', sg.WIN_CLOSED):
        break
    if event == "Entrar":
        usuario = values["-NomeInput-"]+": "
        window["-Tela1-"].update(visible=False)
        window["-Tela2-"].update(visible=True)
    if event == "Enviar":
        texto = values["-InputChat-"]
        chatLog = chatLog + usuario + texto + "\n"
        window["-InputChat-"].update('')
        window["-ChatBox-"].update(chatLog)
    if event == "-VoltarChat-":
        window["-Tela1-"].update(visible=True)
        window["-Tela2-"].update(visible=False)


window.close()