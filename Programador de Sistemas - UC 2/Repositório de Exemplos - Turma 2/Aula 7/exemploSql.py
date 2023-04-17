import psycopg2 # pip install psycopg2

conn = psycopg2.connect(dbname = "Escola", host = "localhost", port="5432", user="postgres", password="postgres") #Porta padrão 5432

cursor = conn.cursor()



cursor.execute('''
SELECT * FROM "Alunos"
ORDER BY "NroMatricula" ASC
''')
# para ver as colunas use o cursor.description
for aluno in cursor.fetchall():
    print(f"{aluno[0]} - {aluno[2]}")


cursor.execute('''
SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'
''')

print(cursor.fetchall())
