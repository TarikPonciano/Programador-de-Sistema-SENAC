from Controle.classConexao import Conexao

import psycopg2

try:
    con = Conexao("Empresa", "localhost", "5432", "postgres", "postgres")
    cursor = con._db.cursor()

    cursor.execute('''SELECT * FROM "Funcionarios" ''')
    print(cursor.fetchall())
    cursor.close()
    con._db.close()
    

except (Exception, psycopg2.Error) as error:
    print("Ocorreu um erro:", error)