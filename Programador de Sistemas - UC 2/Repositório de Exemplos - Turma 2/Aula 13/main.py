from Controle.classConexao import Conexao


def criarTabelas(con):
    listaSql = ['''
    CREATE TABLE "Clientes"(
    "ID" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" varchar(255) NOT NULL,
    "CPF" char(11) NOT NULL UNIQUE
    )
    ''',
                '''
    CREATE TABLE "Livros"(
    "ID" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" varchar(255) NOT NULL,
    "Autor" varchar(255) NOT NULL
    )
    ''',
                '''
    CREATE TABLE "Alugueis"(
    "ID" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "ID_Cliente" int NOT NULL,
    "ID_Livro" int NOT NULL,
    "Data do Aluguel" timestamp default CURRENT_TIMESTAMP(2),
    CONSTRAINT fk_cliente
        FOREIGN KEY("ID_Cliente")
        REFERENCES "Clientes"("ID")
        ,
    CONSTRAINT fk_livro
        FOREIGN KEY("ID_Livro")
        REFERENCES "Livros"("ID")
    )
    '''
                ]

    for sql in listaSql:

        if con.manipularBanco(sql):
            print("Tabela criada.")
        else:
            print("Falha na criação")


def verMenuClientes():

    while True:
        print('''
        Opções menu cliente:

        1. Ver lista de Clientes
        2. Cadastrar Novo Cliente
        3. Atualizar Cliente
        4. Remover Cliente
        0. Voltar ao menu principal

        ''')
        op = input("Escolha uma das opções:")
        match op:
            case "1":
                verListaDeClientes()
            case "2":
                cadastrarNovoCliente()
            case "3":
                atualizarCliente()
            case "4":
                removerCliente()
            case "0":
                print("Voltando ao menu principal...")
                break
            case _:
                print("Escolha uma opção válida.")

        input("Digite Enter para continuar...")


def verListaDeClientes():

    listaClientes = conexaoBanco.consultarBanco('''
    SELECT * FROM "Clientes"
    ORDER BY "ID" ASC
    ''')

    if listaClientes:
        print("ID | NOME | CPF")
        for cliente in listaClientes:
            print(f"{cliente[0]} | {cliente[1]} | {cliente[2]}")

    else:
        print("Ocorreu um erro na consulta, ou a lista é vazia.")


def cadastrarNovoCliente():
    print("Cadastro de Cliente - Insira as informações pedidas")

    nome = input("Digite o nome do Cliente:")
    cpfValido = False

    while cpfValido == False:
        cpf = input("Digite o cpf do Cliente (somente os números):")

        try:
            if len(cpf) == 11 and cpf.isnumeric():
                cpfValido = True
            else:
                print("CPF Inválido, digite novamente. O CPF deve conter 11 digitos e ser somente números.")
                cpfValido = False

        except:

            print("Ocorreu um erro, digite novamente")
            cpfValido = False

    sqlInserir = f'''
    INSERT INTO "Clientes"
    Values(default, '{nome}', '{cpf}')
    '''


    if conexaoBanco.manipularBanco(sqlInserir):

        print(f"O Cliente {nome} foi inserido com sucesso.")
    else:
        print("Falha ao inserir o cliente!")
        

def verMenuLivros():

    while True:
        print('''
        Opções menu livros:

        1. Ver lista de Livros
        2. Cadastrar Novo Livro
        3. Atualizar Livro
        4. Remover Livro
        0. Voltar ao menu principal

        ''')
        op = input("Escolha uma das opções:")
        match op:
            case "1":
                verListaDeLivros()
            case "2":
                cadastrarNovoLivro()
            case "3":
                atualizarLivro()
            case "4":
                removerLivro()
            case "0":
                print("Voltando ao menu principal...")
                break
            case _:
                print("Escolha uma opção válida.")

        input("Digite Enter para continuar...")

def verListaDeLivros():

    listaLivros = conexaoBanco.consultarBanco('''
    SELECT * FROM "Livros"
    ORDER BY "ID" ASC
    ''')

    if listaLivros:
        print("ID | NOME | Autor")
        for livro in listaLivros:
            print(f"{livro[0]} | {livro[1]} | {livro[2]}")

    else:
        print("Ocorreu um erro na consulta, ou a lista é vazia.")

def cadastrarNovoLivro():

    print("Cadastro de Livro - Insira as informações pedidas")

    nome = input("Digite o nome do Livro:")
    autor = input("Digite o nome do Autor:")

    sqlInserir = f'''
    INSERT INTO "Livros"
    Values(default, '{nome}', '{autor}')
    '''

    if conexaoBanco.manipularBanco(sqlInserir):

        print(f"O Livro {nome} foi inserido com sucesso.")
    else:
        print("Falha ao inserir o livro!")

def verMenuAlugueis():
    pass

def cadastrarNovoAluguel():
    pass




    


conexaoBanco = Conexao("Biblioteca", "localhost",
                       "5432", "postgres", "postgres")

while True:

    print('''
    Bem vindo a Biblioteca XYZ

    1. Menu Clientes
    2. Menu Livros
    3. Menu Aluguéis
    0. Sair
    ''')

    op = input("Escolha o menu que deseja acessar:")

    match op:
        case "1":
            verMenuClientes()
        case "2":
            verMenuLivros()
        case "3":
            verMenuAlugueis()
        case "0":
            print("Saindo da aplicação...")
            break
        case _:
            print("Escolha uma opção válida.")
