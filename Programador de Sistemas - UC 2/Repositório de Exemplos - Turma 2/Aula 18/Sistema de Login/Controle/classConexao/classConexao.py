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