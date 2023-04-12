import json

caminhoBanco = "banco.json"


def carregarBanco(endereco, entidade):
    with open(endereco, "r") as bancoJson:

        meuBanco = json.load(bancoJson)

        return meuBanco[entidade]


def menuDepartamentos():

    listaDepartamento = carregarBanco(caminhoBanco, "departamentos")
    print("Lista de Departamentos:")
    print("# || Nome")

    for i, departamento in enumerate(listaDepartamento):

        print(f'{i} || {departamento["Nome"]}')

    escolha = input(
        "Você deseja ver os funcionários de um dos departamentos? (S/N) ")

    if escolha.upper() == "S":

        escolhaDepartamento = int(
            input("Digite o número do departamento escolhido: "))

        departamentoEscolhido = listaDepartamento[escolhaDepartamento]
        idDepartamento = departamentoEscolhido["ID_Departamento"]
        listaFuncionarios = carregarBanco(caminhoBanco, "funcionarios")
        funcionariosDepartamento = []
        chefeDepartamento = None

        for funcionario in listaFuncionarios:
            if idDepartamento == funcionario["ID_Departamento"]:
                funcionariosDepartamento.append(funcionario)
                if departamentoEscolhido["ID_Chefe"] == funcionario["ID_Funcionario"]:
                    chefeDepartamento = funcionario

        print(f'''
Departamento Escolhido:
ID: {departamentoEscolhido["ID_Departamento"]}
Nome: {departamentoEscolhido["Nome"]}
Chefe: {chefeDepartamento["Nome"]}

Lista de Funcionários:
        ''')

        print("# || Nome")
        for i, funcionario in enumerate(funcionariosDepartamento):

            print(f"{i} || {funcionario['Nome']}")

    else:
        print("Voltando para o menu principal...")


def menuFuncionarios():

    listaFuncionario = carregarBanco(caminhoBanco, "funcionarios")
    print("Lista de Funcionários:")
    print("# || Nome")
    for i, funcionario in enumerate(listaFuncionario):

        print(f"{i} || {funcionario['Nome']}")

    # for funcionario in listaFuncionario:

    #     print(f'{funcionario["ID_Funcionario"]}|| {funcionario["Nome"]} || {funcionario["ID_Departamento"]}')
    escolha = input("Deseja ver um funcionário específico (S/N):")

    if escolha.upper() == "S":
        escolhaFuncionario = int(
            input("Digite o número do funcionário desejado:"))
        funcionarioEscolhido = listaFuncionario[escolhaFuncionario]
        meuDepartamento = None

        listaDepartamentos = carregarBanco(caminhoBanco, "departamentos")

        for departamento in listaDepartamentos:

            if departamento["ID_Departamento"] == funcionarioEscolhido["ID_Departamento"]:
                meuDepartamento = departamento

        if funcionarioEscolhido["Nome"] == "Funcionario 5":
            print(f'''
        Funcionário Escolhido:

        ID: {funcionarioEscolhido["ID_Funcionario"]}

        Nome: {funcionarioEscolhido["Nome"]}

        Salario: {funcionarioEscolhido["Salario"]}

        Departamento: {meuDepartamento["Nome"]}
        
        ''')
        else:
            print(f'''
        Funcionário Escolhido:

        ID: {funcionarioEscolhido["ID_Funcionario"]}

        Nome: {funcionarioEscolhido["Nome"]}

        Departamento: {meuDepartamento["Nome"]}
        
        ''')

    else:
        print("Voltando para o menu")


while True:

    print("Bem vindo ao Software de Gerenciamento da Empresa ABC")

    print('''
    
    1. Acessar Funcionários

    2. Acessar Departamentos

    0. Sair
    
    ''')

    op = input("Digite o que deseja fazer: ")

    match op:
        case "1":
            menuFuncionarios()
        case "2":
            menuDepartamentos()
        case "0":
            print("Fechando aplicação...")
            break
        case _:
            print("Digite uma opção válida!")

    input()
