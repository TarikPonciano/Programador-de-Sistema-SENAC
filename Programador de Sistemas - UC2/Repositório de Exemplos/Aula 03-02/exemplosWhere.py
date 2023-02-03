# Símbolos e sintaxe básica do Where: https://www.w3schools.com/sql/sql_where.asp
# Conectores do Where: https://www.w3schools.com/sql/sql_and_or.asp
# Como utilizar o Where: https://www.devmedia.com.br/sql-clausula-where/37645

if __name__ == "__main__":
    import psycopg2
    from Controle.classConexao import Conexao

    try:
        con = Conexao(parametroDb="Empresa", parametroHost="localhost", parametroPort="5432", parametroUser="postgres", parametroPassword="postgres")

        #Consulta básica, pega todos
        funcionarios = con.consultarBanco('''
        SELECT * FROM "Funcionarios"
        ORDER BY "ID" ASC;
        ''')

        for funcionario in funcionarios:
            print(f'''
            {funcionario[0]} - {funcionario[1]} - {funcionario[2]} - {funcionario[3]} - {funcionario[4]}
            ''')

        #Consulta Operador =, usando o ID

        funcionario = con.consultarBanco('''
        SELECT * FROM "Funcionarios"
        WHERE "ID" = 2;
        ''')

        print("Pesquisa por ID:",funcionario)

        #Consulta Operador =, usando o Nome
        # nomePesquisa = input("Digite o nome do Funcionário: ")
        funcionario = con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Nome" = 'Maria';
        ''')

        print("Pesquisa por nome:",funcionario)

        #Consulta Operador >, usando o Salário

        print("Pesquisa por salário:",con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Salário" > '3000'
        ORDER BY "ID"; 
        '''))

        #Consulta Operador <, usando a coluna desejada

        #Consulta Operador >=, usando a coluna desejada

        #Consulta Operador <=, usando a coluna desejada

        #Consulta Operador <>, usando a coluna desejada

        #con._db.close()
        con.fechar()






    
    except(Exception, psycopg2.Error) as error:
        print("Ocorreu um erro", error)