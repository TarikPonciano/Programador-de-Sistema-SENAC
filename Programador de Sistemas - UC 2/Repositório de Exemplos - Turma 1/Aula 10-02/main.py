#Código da tabela utilizada

# CREATE TABLE "Funcionario"(
# "id" int GENERATED ALWAYS AS IDENTITY,
# "nome" varchar(255) NOT NULL,
# "cpf" char(11) NOT NULL UNIQUE
# "idade" int NOT NULL,
# PRIMARY KEY ("id"));



import PySimpleGUI as sg 
import psycopg2
from Controle.classConexao import Conexao
from Modelo.classFuncionario import Funcionario

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

try:
    con = Conexao("TesteEmpresa", "localhost","5432","postgres","postgres")

    print("Deu certo")

except(Exception, psycopg2.Error) as error:
    print("Ocorreu um erro - ")

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
        funcionario = Funcionario("default", values["-InserirNomeFuncionario-"], values["-InserirCpfFuncionario-"], values["-InserirIdadeFuncionario-"] )
        con.manipularBanco(funcionario.inserirFuncionario("Funcionario"))
        sg.popup("Deu Certo!")

window.close()