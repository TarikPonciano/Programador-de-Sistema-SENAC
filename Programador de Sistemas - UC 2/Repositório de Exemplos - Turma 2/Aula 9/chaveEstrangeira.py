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

Conecte as duas tabelas usando a chave Livro_autor como chave estrangeira.
Dica: Se você já tiver criado a tabela Livros, use o comando ALTER

'''
import psycopg2

class Conexao:
    def __init__(self, banco, host, port, user, senha):

        self._banco = banco
        self._host = host
        self._port = port
        self._user = user
        self._senha = senha
    
    def consultarBanco(self,sql):

        conn = psycopg2.connect(dbname=self._banco, host=self._host, port=self._port, user=self._user,password=self._senha )
        cursor = conn.cursor()

        cursor.execute(sql)

        resultado = cursor.fetchall()

        cursor.close()
        conn.close()

        return resultado


    def manipularBanco(self,sql):

        conn = psycopg2.connect(dbname=self._banco, host=self._host, port=self._port, user=self._user,password=self._senha )
        cursor = conn.cursor()

        cursor.execute(sql)

        conn.commit()

        cursor.close()
        conn.close()



def criarTabelaFuncionario():

    sql = '''
    CREATE TABLE "Funcionários"(
    "Id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" varchar(255) NOT NULL,
    "Salário" money NOT NULL default 0,
    "Id_Dept" int NOT NULL default 1,
    CONSTRAINT fk_departamento
        FOREIGN KEY("Id_Dept")
        REFERENCES "Departamentos"("Id")
        ON DELETE NO ACTION
        ON UPDATE NO ACTION


    )
    
    '''
    return sql

def criarTabelaDepartamento():

    sql = '''
    CREATE TABLE "Departamentos"(
    "Id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" varchar(255) NOT NULL

    )
    
    '''
    return sql

conexaoBanco = Conexao("Empresa Exemplo","localhost","5432","postgres","postgres")

while True:

    try:
        print("Cadastro de Funcionário")
        nomeFunc = input("Digite o nome do Funcionário: ")
        salarioFunc = input("Digite o salário do Funcionário: ")
        idDept = input("Digite o departamento: ")

        conexaoBanco.manipularBanco(f'''
        INSERT INTO "Funcionários"
        VALUES(default, '{nomeFunc}', '{salarioFunc}', '{idDept}' )
        
        ''')

    except(Exception, psycopg2.Error) as error:
        print("Ocorreu um erro", error)