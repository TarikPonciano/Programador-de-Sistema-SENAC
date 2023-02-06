#Aula 06-02
#Conteúdo: Revisão Geral de Implementação de Banco de Dados com Python
#Programa: Sistema de Gerenciamento de Biblioteca
#Objetivos:
#   - Criar modelo físico de dados
#   - Entidades: Livros e Clientes Relacionamentos: Aluguel
#   - Criar banco de dados e tabelas
#   - Integrar banco com Python e criar funções de manipulação das tabelas
#   - Ver Clientes, Livros e Alugueis
#   - Inserir Clientes
#   - Registrar Aluguel


import psycopg2
from Controle.classConexao import Conexao
from Modelo.classCliente import Cliente
from Modelo.classLivro import Livro

def criarBancoDeDados(conexao):
    conexao.manipularBanco('''
    DROP DATABASE IF EXISTS "Biblioteca" ;
    CREATE DATABASE "Biblioteca";
    ''')

def criarTabelaCliente(conexao):
    conexao.manipularBanco('''
    DROP TABLE IF EXISTS "Cliente";
    CREATE TABLE "Cliente"(
        "ID" int GENERATED ALWAYS AS IDENTITY,
        "Nome" varchar(255) NOT NULL,
        "CPF" char(11) NOT NULL UNIQUE,
        Primary Key("ID")
    );
    ''')

def criarTabelaLivro(conexao):

    conexao.manipularBanco('''
    DROP TABLE IF EXISTS "Livro";
    CREATE TABLE "Livro(
        "ID" int GENERATED ALWAYS AS IDENTITY,
        "Nome" varchar(255) NOT NULL,
        "Autor" varchar(255) NOT NULL,
        Primary Key("ID")
    );
    ''')

def criarTabelaAluguel(conexao):

    conexao.manipularBanco('''
    DROP TABLE IF EXISTS "Aluguel";
    CREATE TABLE "Aluguel"(
        "ID" int GENERATED ALWAYS AS IDENTITY,
        "ID_Cliente" int NOT NULL,
        "ID_Livro" int NOT NULL,
        "Data_Aluguel" timestamp default current_timestamp,
        Primary Key("ID"),
        Constraint fk_cliente
            Foreign Key ("ID_Cliente")
            References "Cliente"("ID")
            ON DELETE CASCADE
            ON UPDATE NO ACTION
            ,
        Constraint fk_livro
            Foreign Key ("ID_Livro")
            Refereces "Livro"("ID")
            ON DELETE SET NULL
            ON UPDATE NO ACTION
            
    );
    ''')

def menuClientes(conexao):
    print("Lista de clientes: ")
    resultado = conexao.consultarBanco('''
    Select * FROM "Cliente"
    ORDER BY "ID" ASC
    ''')
    print("ID | Nome")
    for cliente in resultado:
        print(f"{cliente[0]} | {cliente[1]}")

    print(f'''
    Escolha uma das opções:
    1. Ver cliente específico
    2. Inserir novo cliente
    0. Voltar para o menu principal
    ''')
    opcoes = input("Digite o número da opção desejada:")
    match opcoes:
        case "1":
            while True:
                clienteID = input("Digite o ID do cliente")
                clienteEscolhido = Cliente(clienteID, None, None)
                resultado = conexao.consultarBanco(clienteEscolhido.consultarClientePorID())
                if resultado != []:
                    clienteEscolhido._nome = resultado[0][1]
                    clienteEscolhido._cpf = resultado[0][2]
                    clienteEscolhido.imprimirCliente()

                    while True:
                        print(f'''
                        Escolha uma das opções:
                        1. Ver alugueis
                        0. Voltar para o menu principal
                        ''')
                        opcoes = input("Digite o numero da opção:")
                        match opcoes:
                            case "1":
                                print(f"Alugueis do Cliente {clienteEscolhido._nome}")
                                resultado = conexao.consultarBanco(clienteEscolhido.consultarAlugueis())
                                if resultado != []:
                                    
                                    print("ID | Livro | Data")
                                    for aluguel in resultado:
                                        livro = Livro(aluguel[2],None, None)
                                        livroAlugado = conexao.consultarBanco(livro.consultarLivroPorID())[0]
                                        livro._nome = livroAlugado[1]
                                        livro._autor = livroAlugado[2]
                                        print(f"{aluguel[0]} | {livro._nome} | {aluguel[3]}")
                                else:
                                    print("Esse usuário não possui alugueis")
                                input("Tecle ENTER para continuar")
                            case "0":
                                print("Saindo do menu cliente.")
                                break
                            case _:
                                print("Você escolheu uma opção inválida")

                    break
                else:
                    print("Você escolheu um ID inválido")
        case "2":
            while (True):
                novoCliente = Cliente(None,None,None)
                novoCliente._nome = input("Digite o nome do cliente:")
                novoCliente._cpf = input("Digite o cpf do cliente:")
                #Sugestão novoCliente.setCPF(input("Digite o cpf do cliente:")
                conexao.manipularBanco(novoCliente.inserirCliente())
                print("Novo cliente inserido")
                break

def menuLivros(conexao):
    print("Lista de Livros: ")
    resultado = conexao.consultarBanco('''
    Select * FROM "Livro"
    ORDER BY "ID" ASC
    ''')
    print("ID | Nome ")
    for livro in resultado:
        print(f"{livro[0]} | {livro[1]}")

    print(f'''
    Escolha uma das opções:
    1. Ver livro específico
    2. Inserir novo livro
    0. Voltar para o menu principal
    ''')
    opcoes = input("Digite o número da opção desejada:")
    match opcoes:
        case "1":
            while True:
                livroID = input("Digite o ID do livro")
                livroEscolhido = Livro(livroID, None, None)
                resultado = conexao.consultarBanco(livroEscolhido.consultarLivroPorID())
                if resultado != []:
                    livroEscolhido._nome = resultado[0][1]
                    livroEscolhido._autor = resultado[0][2]
                    livroEscolhido.imprimirLivro()

                    while True:
                        print(f'''
                        Escolha uma das opções:
                        1. Ver alugueis
                        0. Voltar para o menu principal
                        ''')
                        opcoes = input("Digite o numero da opção:")
                        match opcoes:
                            case "1":
                                print(f"Alugueis do Livro {livroEscolhido._nome}")
                                resultado = conexao.consultarBanco(livroEscolhido.consultarAlugueis())
                                if resultado != []:
                                    
                                    print("ID | Cliente | Data")
                                    for aluguel in resultado:
                                        cliente = Cliente(aluguel[1],None, None)
                                        clienteAlugado = conexao.consultarBanco(cliente.consultarClientePorID())[0]
                                        cliente._nome = clienteAlugado[1]
                                        cliente._cpf = clienteAlugado[2]
                                        print(f"{aluguel[0]} | {cliente._nome} | {aluguel[3]}")
                                else:
                                    print("Esse livro ainda não foi alugado")
                                input("Tecle ENTER para continuar")
                            case "0":
                                print("Saindo do menu livros.")
                                break
                            case _:
                                print("Você escolheu uma opção inválida")

                    break
                else:
                    print("Você escolheu um ID inválido")
        case "2":
            while (True):
                novoLivro = Livro(None,None,None)
                novoLivro._nome = input("Digite o nome do livro:")
                novoLivro._autor = input("Digite o nome do autor:")
                
                conexao.manipularBanco(novoLivro.inserirLivro())
                print("Novo livro inserido")
                break

def menuAlugueis(conexao):
    print("Lista de Alugueis: ")
    resultado = conexao.consultarBanco('''
    Select * FROM "Aluguel"
    ORDER BY "ID" ASC
    ''')
    print("ID | Cliente | Livro | Data ")
    for aluguel in resultado:

        cliente = Cliente(aluguel[1], None, None)
        clienteDoAluguel = conexao.consultarBanco(cliente.consultarClientePorID())[0]
        cliente._nome = clienteDoAluguel[1]
        cliente._cpf = clienteDoAluguel[2]

        livro = Livro(aluguel[2], None, None)
        livroDoAluguel = conexao.consultarBanco(livro.consultarLivroPorID())[0]
        livro._nome = livroDoAluguel[1]
        livro._autor = livroDoAluguel[2]

        print(f"{aluguel[0]} | {cliente._nome} | {livro._nome} | {aluguel[3]}")

    print(f'''
    Escolha uma das opções:
    1. Cadastrar novo aluguel
    0. Voltar para o menu principal
    ''')
    opcoes = input("Digite o número da opção desejada:")
    match opcoes:
        case "1":
            print("Cadastro de aluguel.")

            print("Escolha um Cliente:")

            resultado = conexao.consultarBanco('''
            Select * FROM "Cliente"
            ORDER BY "ID" ASC
            ''')
            print("ID | Nome")

            for cliente in resultado:
                print(f"{cliente[0]} | {cliente[1]}")

            clienteID = input("Digite o id do cliente escolhido: ")

            print("Escolha um Livro:")
            resultado = conexao.consultarBanco('''
            Select * FROM "Livro"
            ORDER BY "ID" ASC
            ''')
            print("ID | Nome")
            for livro in resultado:
                print(f"{livro[0]} | {livro[1]}")

            livroID = input("Digite o id do livro escolhido: ")

            conexao.manipularBanco(f'''
            INSERT INTO "Aluguel"
            Values(default, {clienteID}, {livroID}, default)
            ''')

            print("Aluguel cadastrado.")

        

                



while True:
    try:
        login = input("Insira seu login:")
        password = input("Insira sua senha:")
        # login = "postgres"
        # password = "postgres"
        con = Conexao("Biblioteca","localhost","5432",login,password)
        break

    except (Exception, psycopg2.Error) as error:
        print("Ocorreu um erro -", error)


while True:
    try:
        print("Bem vindo a biblioteca 'Biblioteca dos Livros' ")

        print(f'''
    Escolha uma das opções:

    1. Ver Clientes
    2. Ver Livros
    3. Ver Alugueis
    0. Sair
        
        ''')
        opcoes = input("Digite o número da opção do menu:")

        match opcoes:
            case "1":
                menuClientes(con)
            case "2":
                menuLivros(con)
            case "3":
                menuAlugueis(con)
            case "0":
                print("Saindo da aplicação...")
                break
            case _:
                print("Você digitou uma opção inválida.")

        input("Pressione qualquer tecla para continuar")

        
    
    except (Exception, psycopg2.Error) as error:
        print("Ocorreu um erro -",error)

con.fechar()