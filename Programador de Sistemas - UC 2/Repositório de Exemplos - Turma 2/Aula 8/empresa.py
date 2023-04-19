# Deve conter as seguintes entidades Funcionários e Departamentos
# Requisitos:
# - Ver lista de funcionários
# - Ver lista de departamentos
# - Ver informações de funcionários específico(Deve conter o Departamento de que faz parte)
# - Ver lista de funcionários de um departamento específico
# - Opcional: Funcionário gerente e autenticação antes de usar o sistema
# - Inserção de Funcionários e Departamentos
# - Atualização de informações de Funcionários e Departamentos
# - Remoção de Funcionários e Departamentos

#Entidade Funcionário:

# Id_Func: integer AUTO GENERATED (PK)
# Nome_Func: char(255) NOT NULL
# Salário_Func: float(2) NOT NULL default 0.00
# Cargo_Func: char(255) NOT NULL default Autônomo
# Id_Departamento: integer (FK)

#Entidade Departamento:

# Id_Departamento: integer AUTO GENERATED (PK)
# Nome_Departamento: char(255)
# #Id_Gerente: integer (FK) (OPCIONAL)

import psycopg2


#Funções com código de criação das tabelas - Deve ser rodado apenas 1 vez
def criarTabelaFuncionario():
    sql = '''
    CREATE TABLE "Funcionário"(
    "Id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" varchar(255) NOT NULL,
    "Salário" money NOT NULL default 0,
    "Cargo" varchar(255) NOT NULL default 'Autônomo',
    "Id_Dept" int NOT NULL default 1
    )
    ''' 
    return sql

def criarTabelaDepartamento():

    sql = '''
    CREATE TABLE "Departamentos"(
    "Id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" varchar(255) NOT NULL
    -- "Id_Gerente" int NOT NULL default 1
    )
    ''' 
    return sql

try:
    conn = psycopg2.connect(dbname="XYZ Soluções", host="localhost",port="5432",user="postgres", password="postgres")
    
    cursor = conn.cursor()

    cursor.execute(criarTabelaFuncionario())
    conn.commit()

    cursor.execute(criarTabelaDepartamento())
    conn.commit()

    print("Tabelas criadas.")


# Código para verificar tabelas que existem no seu DB
#     cursor.execute('''
#     SELECT table_name
#   FROM information_schema.tables
#  WHERE table_schema='public'
#    AND table_type='BASE TABLE';
#     ''') 

#     print(cursor.fetchall())

    cursor.close()

    conn.close()

except(Exception, psycopg2.Error) as error:
    print("Ocorreu um erro ao tentar a conexão:", error)



