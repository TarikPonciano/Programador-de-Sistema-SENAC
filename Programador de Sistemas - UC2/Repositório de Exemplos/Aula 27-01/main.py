# Funcionarios:

# Func_id - serial PRIMARY KEY
# Func_nome - varchar(255)
# Func_cpf - char(11) UNIQUE NOT NULL
# Func_salario - money

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
    idFunc = int(input("Digite o id do funcionário que deseja modificar: "))
    novoNome = input("Digite o novo nome: ")
    novoSalario = float(input("Digite o novo salário:"))

    cur.execute(f'''
    UPDATE "Funcionarios"
    SET "Nome" = '{novoNome}', "Salário" = {novoSalario}
    WHERE "ID" = {idFunc}
    ''')
    conexao.commit()

def removerFuncionario(cur, conexao):
    idFunc = int(input("Digite o id do funcionário que deseja remover: "))
    cur.execute(f'''
    DELETE FROM "Funcionarios"
    WHERE "ID" = {idFunc}
    ''')
    conexao.commit()

def listarFuncionario(cur, conexao):

    cur.execute('''
    SELECT * FROM "Funcionarios"
    ''')
    print(cur.fetchall())


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