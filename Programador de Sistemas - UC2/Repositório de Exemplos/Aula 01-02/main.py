from Controle.classConexao import Conexao

import psycopg2

try:
    con = Conexao("Empresa", "localhost", "5432", "postgres", "postgres")

    

except (Exception, psycopg2.Error) as error:
    print("Ocorreu um erro:", error)