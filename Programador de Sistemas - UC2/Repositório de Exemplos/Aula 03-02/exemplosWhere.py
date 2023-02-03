# Símbolos e sintaxe básica do Where: https://www.w3schools.com/sql/sql_where.asp
# Conectores do Where: https://www.w3schools.com/sql/sql_and_or.asp
# Como utilizar o Where: https://www.devmedia.com.br/sql-clausula-where/37645

if __name__ == "__main__":
    import psycopg2
    from Controle.classConexao import Conexao

    try:
        print("Código aqui")

    
    except(Exception, psycopg2.Error) as error:
        print("Ocorreu um erro", error)