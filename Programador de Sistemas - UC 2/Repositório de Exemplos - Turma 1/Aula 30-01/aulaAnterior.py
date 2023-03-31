# Funcionarios:

# Func_id - serial PRIMARY KEY
# Func_nome - varchar(255)
# Func_cpf - char(11) UNIQUE NOT NULL
# Func_salario - money

'''Atividade para casa:
Crie uma banco de dados de uma Biblioteca que deverá conter a seguinte tabela:

Livros:

Livro_id
Livro_nome
Livro_paginas
Livro_anoLançamento
Livro_autor

- Especificar os tipos de cada atributo e criar função no python createTableLivros
- Usar o código abaixo para criar um CRUD, sistema de gerenciamento da tabela

CRUD significa Create, Read, Update, Delete e se refere as operações básicas que podemos realizar
com os campos de um tabela de um banco de dados.

Create - Inserir um novo campo. Exemplo: Inserir um novo funcionário na tabela Funcionários
Read - Relacionado ao comando Select, é o ato de ler e imprimir todos os campos ou campos específicos de uma tabela
Update - Atualizar um campo da tabela
Delete - Remover uma entrada da tabela. Ex: Remover um funcionário


'''

import psycopg2 #Para instalar > pip install psycopg2 

def createTableFuncionario(cur,conexao):

    cur.execute('''
    CREATE TABLE "Funcionarios"(
    "ID" serial,
    "Nome" varchar(255),
    "CPF" char(11) UNIQUE NOT NULL,
    "Salário" money DEFAULT 0.00,
    PRIMARY KEY("ID")
    );
    ''')
    conexao.commit()

def inserirFuncionario(cur,conexao):
    novoNome = input("Insira o nome do novo funcionário: ")

    while True:
        novoCpf = input("Insira o CPF do novo funcionário: ")
        if len(novoCpf) != 11:
            print("Tamanho inválido, o cpf precisa conter 11 digitos")
        else:
            break
        
    novoSalario = input("Insira o Salário do novo funcionário: ")
    cur.execute(f'''
    INSERT INTO "Funcionarios"
    VALUES(default, '{novoNome}', '{novoCpf}', {novoSalario})
    ''')
    conexao.commit()

def atualizarFuncionario(cur,conexao):
    listarFuncionario(cur,conexao)
    idFunc = int(input("Digite o id do funcionário que deseja modificar: "))

    cur.execute(f'''
        SELECT * FROM "Funcionarios"
        WHERE "ID" = {idFunc}
    ''')
    print("Funcionario escolhido:",cur.fetchone())

    novoNome = input("Digite o novo nome: ")

    while True:
        novoCpf = input("Insira o novo CPF do funcionário: ")
        if len(novoCpf) != 11:
            print("Tamanho inválido, o cpf precisa conter 11 digitos")
        else:
            break

    novoSalario = float(input("Digite o novo salário:"))

    cur.execute(f'''
    UPDATE "Funcionarios"
    SET "Nome" = '{novoNome}', "Salário" = {novoSalario}, "CPF" = '{novoCpf}'
    WHERE "ID" = {idFunc}
    ''')
    conexao.commit()

def removerFuncionario(cur, conexao):
    listarFuncionario(cur,conexao)
    idFunc = int(input("Digite o id do funcionário que deseja remover: "))
    cur.execute(f'''
        SELECT * FROM "Funcionarios"
        WHERE "ID" = {idFunc}
    ''')
    print("Funcionario escolhido:",cur.fetchone())
    cur.execute(f'''
    DELETE FROM "Funcionarios"
    WHERE "ID" = {idFunc}
    ''')
    conexao.commit()

def listarFuncionario(cur, conexao):

    cur.execute('''
    SELECT * FROM "Funcionarios"
    ''')
    funcionarios = cur.fetchall()
    print("ID | Nome | CPF | Salário")
    for funcionario in funcionarios:
        print(f"{funcionario[0]} | {funcionario[1]} | {funcionario[2]} | {funcionario[3]}")


while True:
    try:

        con = psycopg2.connect(database="Empresa",user="postgres", password="postgres", host="localhost", port="5432")
        #(database="Empresa",user="postgres", password="postgres", host="localhost", port="5432")

        cursor = con.cursor()
        print("Conectado")

        print('''
        1. Ver funcionários
        2. Inserir funcionário
        3. Modificar funcionario
        4. Remover funcionário
        0. Sair do Programa
        ''')

        opcaoMenu = input("Escolha o que deseja fazer: ")

        match opcaoMenu:
            case "1":
                listarFuncionario(cursor, con)
            case "2":
                inserirFuncionario(cursor, con)
            case "3":
                atualizarFuncionario(cursor, con)
            case "4":
                removerFuncionario(cursor, con)
            case "0":
                print("Você escolheu sair da aplicação. Até mais!")
                break
            case _:
                print("Você inseriu algum valor inválido.")

        input("Tecle Enter para prosseguir")

        cursor.close()
        con.close()

    except(Exception, psycopg2.Error) as error:
        print("Ocorreu um erro -", error)
