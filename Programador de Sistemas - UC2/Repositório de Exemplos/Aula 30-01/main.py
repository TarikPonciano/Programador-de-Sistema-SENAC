# Funcionarios:

# Func_id - int GENERATED ALWAYS AS IDENTITY PRIMARY KEY
# Func_nome - varchar(255)
# Func_cpf - char(11) #UNIQUE NOT NULL#
# Func_salario - money
# Dept_id - int
# CONSTRAINT fk_departamento
#   FOREIGN KEY ("ID_Dept")
#   REFERENCES "Departamento"("ID")
#   ON DELETE CASCADE, SET NULL, SET DEFAULT, NO ACTION
#   ON UPDATE NO ACTION

# Departamentos:

# Dept_id - int GENERATED ALWAYS AS IDENTITY PRIMARY KEY
# Dept_nome - varchar(255)

'''Atividade para casa:
Crie uma banco de dados de uma Biblioteca que deverá conter a seguinte tabela:

Livros:

Livro_id (PK)
Livro_nome
Livro_paginas
Livro_anoLançamento
Livro_autor (FK)

Autores:

Autor_id (PK)
Autor_nome

Conecte as duas tabelas usando a chave Livro_autor como chave estrangeira.]
Dica: Se você já tiver criado a tabela Livros, use o comando ALTER

'''

import psycopg2

def createTableFuncionarios(cursor,conexao):
    cursor.execute('''
    DROP TABLE IF EXISTS "Funcionarios";

    CREATE TABLE "Funcionarios"(
        "ID" int GENERATED ALWAYS AS IDENTITY,
        "Nome" varchar(255) NOT NULL,
        "CPF" char(11),
        "Salário" money,
        "ID_Departamento" int,
        CONSTRAINT fk_departamento
            FOREIGN KEY("ID_Departamento")
            REFERENCES "Departamentos"("ID")
            ON DELETE NO ACTION 
            ON UPDATE NO ACTION
            ,

        PRIMARY KEY ("ID")
    );
    ''')

    # cur.execute('''
    # ALTER TABLE "Funcionarios"
    #     DROP CONSTRAINT fk_departamento IF EXISTS,
    #     ADD CONSTRAINT fk_departamento
    #         FOREIGN KEY (ID_Departamento)
    #         REFERENCES "Departamentos"("ID")
    #         ON DELETE CASCADE;

    # ''') Código para alterar o comportamento do ON DELETE de um Constraint

    con.commit()

def createTableDepartamentos(cursor,conexao):
    cursor.execute('''
    DROP TABLE IF EXISTS "Departamentos";

    CREATE TABLE "Departamentos"(
        "ID" int GENERATED ALWAYS AS IDENTITY,
        "Nome" varchar(255),
        PRIMARY KEY("ID")
    );
    
    ''')
    conexao.commit()

def inserirFuncionario(cursor, conexao):
    novoNome = input("Digite o nome do funcionário: ")
    novoCPF = input("Digite o CPF se existir: ")
    novoSalario = input("Digite o salário do funcionário: ")
    departamento = input("Digite o id do departamento: ")

    cursor.execute(f'''

    INSERT INTO "Funcionarios"
    VALUES(default,'{novoNome}','{novoCPF}','{novoSalario}','{departamento}');
    
    ''')
    conexao.commit()

def inserirDepartamento(cursor, conexao):
    novoDepartamento = input("Digite o nome do novo Departamento: ")
    cursor.execute(f'''

    INSERT INTO "Departamentos"
    VALUES(default,'{novoDepartamento}');
    
    ''')
    conexao.commit()

def verFuncionario(cursor, conexao):

    idFunc = input("Digite o id do Funcionário: ")
    cursor.execute(f'''
    SELECT * FROM "Funcionarios"
    Where "ID" = {idFunc}
    ''')
    funcionario = cursor.fetchall()[0]
    idDepartamento = funcionario[4]
    cursor.execute(f'''
    SELECT * FROM "Departamentos"
    WHERE "ID" = {idDepartamento}
    ''')
    departamento = cursor.fetchall()[0]
    print(f'''
    Funcionário:

    ID - {funcionario[0]}
    Nome - {funcionario[1]}
    CPF - {funcionario[2]}
    Salário - {funcionario[3]}

    Departamento:

    ID - {departamento[0]}
    Nome - {departamento[1]}
    
    ''')

def verFuncionarioMelhor(cursor, conexao):
    idFunc = input("Digite o id do Funcionário: ")
    cursor.execute(f'''
    SELECT * FROM "Funcionarios"
    INNER JOIN "Departamentos"
    ON "Funcionarios"."ID_Departamento" = "Departamentos"."ID"
    Where "Funcionarios"."ID" = {idFunc}
    ''')
    funcionario = cursor.fetchall()[0]

    print(f'''
    Funcionário:

    ID - {funcionario[0]}
    Nome - {funcionario[1]}
    CPF - {funcionario[2]}
    Salário - {funcionario[3]}

    Departamento:

    ID - {funcionario[5]}
    Nome - {funcionario[6]}
    
    ''')


try: 
    con = psycopg2.connect(database="Empresa", user="postgres", password="postgres", host="localhost", port="5432")
    cur = con.cursor()
    cur.execute('''
    Select * From "Funcionarios"
    ''')
    print(cur.fetchall())
    cur.execute('''
    Select * From "Departamentos"
    ''')
    print(cur.fetchall())
    verFuncionarioMelhor(cur,con)
    cur.close()
    con.close()

except (Exception, psycopg2.Error) as error:
    print("Ocorreu um erro:", error)
