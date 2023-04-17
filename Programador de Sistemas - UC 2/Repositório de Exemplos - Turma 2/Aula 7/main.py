import psycopg2

try:
    conn = psycopg2.connect(dbname="Escola 2", host="localhost", port="5432", user="postgres", password="postgres")

    cursor = conn.cursor()
    
    print("Conectado com sucesso!")

    # cursor.execute('''
    # CREATE TABLE "Alunos"(
    # "NroMatricula" serial,
    # "Nome" varchar(255) NOT NULL,
    # "CPF" char(11) NOT NULL,
    # "Endereço" varchar(255) default 'Não Informado',
    # "Telefone" char(11) default 'xx-xxxx',
    # "Ano Nascimento" integer,
    # Primary Key ("NroMatricula")
    # );
    
    # ''')

    # conn.commit()

    cursor.execute('''
    INSERT INTO "Alunos"
    Values(default, 'Julio', '12345678910', default, default, 2005)
    ''')

    conn.commit()

    cursor.execute('Select * FROM "Alunos"')

    for aluno in cursor.fetchall():

        print(aluno[1])

    conn.close()



except(Exception, psycopg2.Error) as error:
    print("Ocorreu um erro!", error)
    
