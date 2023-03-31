import psycopg2

try:
    con = psycopg2.connect(database="banconinho",user="postgres",password="postgres",host="localhost",port="5432")
    print("Conectado ao banco de dados")
    cursor = con.cursor()

    cursor.execute('''
    DELETE FROM
    "Alunos2"
    WHERE "nome" = 'Marcio'
    ''')
    con.commit()

    cursor.execute('''
    INSERT INTO "Alunos2"
    VALUES(default, '22222', 'Emilio')
    
    ''')
    con.commit()


    cursor.execute('''
        SELECT * FROM "Alunos2"
    ''')
    

    alunos = cursor.fetchall()

    for aluno in alunos:
        print(f'''
        Nro Matricula - {aluno[0]}
        CPF - {aluno[1]}
        Nome - {aluno[2]}
        ''')

    con.commit()
    
    con.close()
except:
    print("Deu errado")