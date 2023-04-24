# Símbolos e sintaxe básica do Where: https://www.w3schools.com/sql/sql_where.asp
# Conectores do Where: https://www.w3schools.com/sql/sql_and_or.asp
# Como utilizar o Where: https://www.devmedia.com.br/sql-clausula-where/37645


#Utilizando os exemplos abaixo, crie uma consulta para cada uma das situações
#propostas abaixo fazendo uso do comando WHERE.
import psycopg2

try:
    conn = psycopg2.connect(dbname="XYZ Soluções", host="localhost",
                            port="5432", user="postgres", password="postgres")

    cursor = conn.cursor()

except (Exception, psycopg2.Error) as error:
    print("Ocorreu um erro", error)


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