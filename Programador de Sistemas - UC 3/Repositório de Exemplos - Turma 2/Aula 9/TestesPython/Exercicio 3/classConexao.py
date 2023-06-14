import psycopg2
import dotenv
import os

dotenv.load_dotenv()

class Conexao():
    def __init__(self):

        self.host = os.getenv("HOSTDB")
        self.port = os.getenv("PORTDB")
        self.dbname = os.getenv("DBNAME")
        self.user = os.getenv("USERDB")
        self.password = os.getenv("PASSWORDDB")

    def consultarBanco(self,sql):
        try:
            con = psycopg2.connect(host=self.host,port=self.port,dbname=self.dbname,user=self.user,password=self.password)

            cursor = con.cursor()

            cursor.execute(sql)

            resultado = cursor.fetchall()

            cursor.close()
            con.close()

            return resultado
        except(Exception, psycopg2.Error) as error:

            msg = f"Ocorreu um erro {error}"

            print(msg)

            return False
        
    def manipularBanco(self,sql):
        try:
            con = psycopg2.connect(host=self.host,port=self.port,dbname=self.dbname,user=self.user,password=self.password)

            cursor = con.cursor()

            cursor.execute(sql)

            con.commit()

            cursor.close()
            con.close()

            return True
        except(Exception, psycopg2.Error) as error:

            msg = "Ocorreu um erro "+error

            print(msg)
            
            return False
        