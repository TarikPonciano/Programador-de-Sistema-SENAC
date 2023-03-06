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

        print("Pesquisa por ID igual:",funcionario)

        #Consulta Operador =, usando o Nome
        # nomePesquisa = input("Digite o nome do Funcionário: ")
        funcionario = con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Nome" = 'Maria';
        ''')

        print("Pesquisa por nome igual:",funcionario)

        #Consulta Operador >, usando o Salário

        print("Pesquisa por salário maior:",con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Salário" > '3000'
        ORDER BY "ID"ASC; 
        '''))

        #Consulta Operador <, usando a coluna desejada

        print("Pesquisa por Salário menor:",con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Salário" < '5000'
        ORDER BY "ID" ASC; 
        '''))

        #Consulta Operador >=, usando a coluna desejada
        
        print("Pesquisa por nome Maior ou Igual:",con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Nome" >= 'Maria'
        ORDER BY "ID" ASC; 
        '''))


        #Consulta Operador <=, usando a coluna desejada

        print("Pesquisa por salário Menor ou Igual:",con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Salário" <= '5000'
        ORDER BY "ID" ASC; 
        '''))

        #Consulta Operador <>, usando a coluna desejada

        print("Pesquisa por nome diferente:",con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Nome" <> 'Maria'
        ORDER BY "ID" ASC; 
        '''))

        #Consulta Operador Between

        print("Pesquisa por Salário entre valor: ",con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Salário" BETWEEN '2000' AND '5000'
        '''))

        #Consulta Operador IN

        print("Pesquisa por lista de nomes: ",con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Nome" IN ('Maria', 'Matheus', 'Roberta')
        '''))

        #Consulta Operador Like

        print("Pesquisa por nome: ",con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Nome" LIKE '%Mar%'
        '''))

        #'Mar%' - Pesquisar Mar no começo do nome
        #'%Mar%' - Pesquisar Mar em qualquer parte do nome
        #'%Mar' - Pesquisar Mar no final do nome

        #Consulta Operador Not

        print("Pesquisa por nome: ",con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Nome" NOT LIKE '%Mar%'
        '''))

        print("Pesquisa por nome: ",con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Nome" NOT IN ('Roberta', 'Matheus')
        '''))

        

        #Consulta Operador NoT
        #con._db.close()
        con.fechar()


    
    except(Exception, psycopg2.Error) as error:
        print("Ocorreu um erro", error)