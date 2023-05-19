# import sys

# sys.path.append("C:\Tarik\Github\Programador-de-Sistema-SENAC\Programador de Sistemas - UC 2\Repositório de Exemplos - Turma 2\Aula 18\Sistema de Login\Controle\classConexao")

# import classConexao

import psycopg2 

class Conexao:

    def __init__(self,dbname,host,port,user,password):
        self.dbname=dbname
        self.host=host
        self.port=port
        self.user=user
        self.password=password

    def consultarBanco(self,sql):
        try:
            con=psycopg2.connect(dbname=self.dbname, host=self.host, port=self.port,user=self.user,password=self.password)

            cursor = con.cursor()

            cursor.execute(sql)

            resultado = cursor.fetchall()

            cursor.close()

            con.close()

            return resultado

        except(Exception,psycopg2.Error) as error:
            print("Ocorreu um erro.")




    def manipularBanco(self,sql):

        try:
            con=psycopg2.connect(dbname=self.dbname, host=self.host, port=self.port,user=self.user,password=self.password)

            cursor = con.cursor()

            cursor.execute(sql)

            con.commit()

            cursor.close()

            con.close()

        except(Exception,psycopg2.Error) as error:
            print("Ocorreu um erro.")

conexaoBanco = Conexao("Login Teste", "localhost", "5432", "postgres", "postgres")

def createTableUsuario():

    sql = '''Create Table "Usuarios"(
    "Id" int GENERATED ALWAYS AS IDENTITY Primary Key,
    "Nome" varchar(255),
    "CPF" char(11) UNIQUE,
    "email" varchar(255) UNIQUE,
    "usuário" varchar(255) UNIQUE,
    "senha" varchar(255)
    )'''

    conexaoBanco.manipularBanco(sql)

logado = False

while True:

    login = input("Digite seu email:")

    consultaUsuario = conexaoBanco.consultarBanco(f'''
    SELECT * FROM "Usuarios"
    WHERE "email" = '{login}'
    ''')
    

    if consultaUsuario == []:
        print("Usuário não existe.")
        
    else:
        meuUsuario = consultaUsuario[0]
        senha = input("Digite sua senha:")
        
        if senha == meuUsuario[5]:
            logado = True
            print("Bem vindo", meuUsuario[1])
        else:
            logado = False
            print("Senha incorreta.")

    while logado:

        if meuUsuario[6] == "padrão":

            print('''
            Menu Padrão

            1. Imprimir meu nome
            

            0. Sair
            
            ''')

            op = input("Digite o que deseja fazer:")

            match op:

                case "1":
                    print(meuUsuario[1])


                case "0":
                    logado = False
                    print("Saindo do programa")
        elif meuUsuario[6] == "admin":
            print('''
            Menu Admin

            1. Imprimir meu nome

            0. Sair
            
            ''')

            op = input("Digite o que deseja fazer:")

            match op:

                case "1":
                    print(meuUsuario[1])
                case "0":
                    logado = False
                    print("Saindo do programa")









    
    