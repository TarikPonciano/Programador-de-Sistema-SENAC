import json

# CRUD - Create, Read, Update, Delete


def pegarListaAtualizada():

    with open("funcionario.json", 'r') as funcionariosJson:
        lista = json.load(funcionariosJson)

    return lista


def verFuncionarios():

    listaFuncionarios = pegarListaAtualizada()

    print("Lista de Funcionários: ")

    print("Nome | CPF | Salario | Cargo | Departamento")

    for funcionario in listaFuncionarios:

        print(
            f'{funcionario["nome"]} | {funcionario["cpf"]} | {funcionario["salario"]} | {funcionario["cargo"]} | {funcionario["departamento"]}')

    input()


def inserirFuncionario():

    funcionario = {}

    # for dado in funcionario.keys:

    #     insercao = input(f"Insira o {dado}")

    #     funcionario[dado] = insercao

    print("Inserir Novo Funcionário:")

    nomeFuncionario = input("Insira o nome do Funcionário: ")
    cpfFuncionario = input("Insira o cpf do Funcionario:")
    salarioFuncionario = input("Insira o salario do Funcionario:")
    cargoFuncionario = input("Insira o cargo do Funcionario:")
    departamentoFuncionario = input("Insira o departamento do Funcionario:")

    funcionario["nome"] = nomeFuncionario
    funcionario["cpf"] = cpfFuncionario
    funcionario["salario"] = float(salarioFuncionario)
    funcionario["cargo"] = cargoFuncionario
    funcionario["departamento"] = departamentoFuncionario

    listaFuncionarios = pegarListaAtualizada()
    listaFuncionarios.append(funcionario)

    with open("funcionario.json", 'w') as funcionariosJson:
        json.dump(listaFuncionarios, funcionariosJson, indent=2)


while True:

    print('''
    Bem vindo a Empresa XYZ

    Menu:

    1. Ver Funcionários
    2. Inserir Funcionário
    0. Sair
    
    ''')

    op = input("Escolha uma opção: ")

    match op:
        case "1":
            verFuncionarios()
        case "2":
            inserirFuncionario()
        case "0":
            print("Saindo do Programa...")
            break
