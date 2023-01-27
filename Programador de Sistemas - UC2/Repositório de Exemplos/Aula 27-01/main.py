# Funcionarios:

# Func_id - serial PRIMARY KEY
# Func_nome - varchar(255)
# Func_cpf - char(11) NOT NULL
# Func_salario - money

import psycopg2 #Para instalar > pip install psycopg2 

def createTableFuncionario(cur,conexao):

    cur.execute('''
    CREATE TABLE "Funcionarios2"(
    "ID" serial,
    "Nome" varchar(255),
    "CPF" char(11) NOT NULL,
    "Salário" money DEFAULT 0.00,
    PRIMARY KEY("ID")
    );
    ''')
    conexao.commit()


try:

    con = psycopg2.connect(database="Empresa",user="postgres", password="postgres", host="localhost", port="5432")
    #(database="Empresa",user="postgres", password="postgres", host="localhost", port="5432")

    cursor = con.cursor()
    print("Conectado")

    createTableFuncionario(cursor, con)

    cursor.close()
    con.close()
    print("Tabela Criada")

except(Exception, psycopg2.Error) as error:
    print("Ocorreu um erro -", error)