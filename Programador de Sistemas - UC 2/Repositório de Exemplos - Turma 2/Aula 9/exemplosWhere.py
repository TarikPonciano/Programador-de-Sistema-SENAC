# Símbolos e sintaxe básica do Where: https://www.w3schools.com/sql/sql_where.asp
# Conectores do Where: https://www.w3schools.com/sql/sql_and_or.asp
# Como utilizar o Where: https://www.devmedia.com.br/sql-clausula-where/37645

import psycopg2

try:
    conn = psycopg2.connect(dbname="XYZ Soluções", host="localhost",
                            port="5432", user="postgres", password="postgres")

    cursor = conn.cursor()

except (Exception, psycopg2.Error) as error:
    print("Ocorreu um erro", error)