from Controle.classConexao import Conexao
from Modelo.classFuncionario import Funcionario

import psycopg2

try:
    con = Conexao("Empresa", "localhost", "5432", "postgres", "postgres")

    funcionario = Funcionario(2, "Getulio","05955150374","5000",idDepartamento="3")
    funcionario.imprimirFuncionario()
    con.manipularBanco(funcionario.atualizarFuncionario("Funcionarios"))

    print(con.consultarBanco('''
    SELECT * FROM "Funcionarios"
    
    '''))


    con._db.close()




    

except (Exception, psycopg2.Error) as error:
    print("Ocorreu um erro:", error)