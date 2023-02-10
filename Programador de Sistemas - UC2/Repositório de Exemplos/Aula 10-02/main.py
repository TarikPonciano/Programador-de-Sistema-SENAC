import PySimpleGUI as sg 

sg.theme("DarkAmber")

telaInicial = [[sg.Push(),sg.Text("Bem vindo a empresa 'Empresa'"),sg.Push()],
[sg.Button("Ver Funcionarios",key="-VerFuncionarios-")],
[sg.Button("Inserir Funcionario",key="-InserirFuncionario-")],
[sg.Button("Sair", key="-TelaPrincipalSair-")]]

telaInserir = [[sg.Text("Insira um Funcionario")],
[sg.Text("Nome: "), sg.Input(key="-InserirNomeFuncionario-")],
[sg.Text("CPF: "), sg.Input(key="-InserirCpfFuncionario-")],
[sg.Text("Idade: "), sg.Input(key="-InserirIdadeFuncionario-")],
[sg.Button("Enviar", key="-FuncionarioInserirEnviar-"),sg.Button("Voltar", key="-FuncionarioInserirVoltar-")]
]

layout = [[sg.Column(telaInicial, key="-TelaInicial-", visible=True), sg.Column(telaInserir, key="-TelaInserir-",visible=False)]]

window = sg.Window("Sistema de Gestão", layout)

while True:

    event, values = window.read()

    if event in ("-TelaPrincipalSair-", sg.WIN_CLOSED):
        break
    if event == "-InserirFuncionario-":
        window['-TelaInicial-'].update(visible=False)
        window['-TelaInserir-'].update(visible=True)

    if event =="-FuncionarioInserirVoltar-":
        window['-TelaInicial-'].update(visible=True)
        window['-TelaInserir-'].update(visible=False)
    
    if event =="-FuncionarioInserirEnviar-":
        nomeFuncionario = values["-InserirNomeFuncionario-"]
        cpfFuncionario = values["-InserirCpfFuncionario-"]
        idadeFuncionario = values["-InserirIdadeFuncionario-"]

        print(f'''
        Nome: {nomeFuncionario}
        CPF: {cpfFuncionario}
        Idade: {idadeFuncionario}
        ''')

window.close()