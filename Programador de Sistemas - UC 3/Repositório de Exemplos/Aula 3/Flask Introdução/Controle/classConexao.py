import psycopg2

class Conexao():

    def __init__(self, parametroDb, parametroHost,parametroPort,parametroUser,parametroPassword):
        self.parametroDb = parametroDb
        self.parametroHost = parametroHost
        self.parametroPort = parametroPort
        self.parametroUser = parametroUser
        self.parametroPassword = parametroPassword

    def manipularBanco(self, sql):

        try:
            con = psycopg2.connect(database=self.parametroDb, host=self.parametroHost, port=self.parametroPort, user=self.parametroUser, password=self.parametroPassword)

            cursor = con.cursor()

            cursor.execute(sql)

            con.commit()

            cursor.close()

            con.close()

            return "Deu certo"
        
        except(Exception,psycopg2.Error) as error:
            con.close()
            return f"Ocorreu um erro {error}"
        
    def consultarBanco(self,sql):
        try:
            con = psycopg2.connect(database=self.parametroDb, host=self.parametroHost, port=self.parametroPort, user=self.parametroUser, password=self.parametroPassword)
            cursor = con.cursor()
            
            cursor.execute(sql)

            resultado = cursor.fetchall()

            cursor.close()
            con.close()
            return resultado
        except(Exception, psycopg2.Error) as error:
            con.close()

            return f"Ocorreu um erro {error}"
