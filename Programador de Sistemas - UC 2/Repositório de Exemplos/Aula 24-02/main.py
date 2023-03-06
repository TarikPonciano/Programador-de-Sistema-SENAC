#Objetivos

# 1. Visualizar as tabelas Cliente, Livro e Aluguel
# 2. Visualizar na tabela aluguel o nome do Cliente e do Livro daquele aluguel

import psycopg2
from Controle.classConexao import Conexao


def verClientes(conexao):

    clientes = conexao.consultarBanco('''
    Select * FROM "Cliente"
    ORDER BY "ID" ASC
    ''')
    print("ID | Nome")

    for cliente in clientes:

        print(f'{cliente[0]} | {cliente[1]}')

def verLivros(conexao):

    livros = conexao.consultarBanco('''
    Select * FROM "Livro"
    ORDER BY "ID" ASC
    ''')
    print("ID | Nome")

    for livro in livros:

        print(f'{livro[0]} | {livro[1]}')

def verAlugueisSimples(conexao):

    alugueis = conexao.consultarBanco('''
    Select * FROM "Aluguel"
    ORDER BY "ID" ASC
    ''')
    print("ID Aluguel | ID Cliente | ID Livro | Data de Aluguel")

    for aluguel in alugueis:

        print(f'{aluguel[0]} | {aluguel[1]} | {aluguel[2]} | {aluguel[3]}')

def verAlugueisCompleto(conexao):

    alugueis = conexao.consultarBanco('''
    Select * FROM "Aluguel"
    ORDER BY "ID" ASC
    ''')
    print("ID Aluguel | Nome Cliente | Nome Livro | Data de Aluguel")

    for aluguel in alugueis:

        nomeDoCliente = conexao.consultarBanco(f'''
        SELECT "Nome" FROM "Cliente"
        WHERE "ID" = {aluguel[1]}
        ''')[0][0]

        nomeDoLivro = conexao.consultarBanco(f'''
        SELECT "Nome" FROM "Livro"
        WHERE "ID" = {aluguel[2]}
        ''')[0][0]
        
        print(f'{aluguel[0]} | {nomeDoCliente} | {nomeDoLivro} | {aluguel[3]}')



try:

    con = Conexao("Biblioteca","localhost","5432","postgres","postgres")

    while True:

        print('''Bem vindo a Biblioteca
        
        Menu:

        1. Ver Clientes
        2. Ver Livros
        3. Ver Alugueis (Simples)
        4. Ver Alugueis (Completo)
        0. Sair
        
        ''')

        opcoes = input("Digite a opção escolhida: ")

        match opcoes:
            case "1":
                verClientes(con)
            case "2":
                verLivros(con)
            case "3":
                verAlugueisSimples(con)
            case "4":
                verAlugueisCompleto(con)
            case "0":
                break
            case _:
                print("Você escolheu uma opção inválida!\n")

        input("Tecle Enter para continuar.")
    con.fechar()


except(Exception, psycopg2.Error) as error:

    print("Ocorreu um erro", error)