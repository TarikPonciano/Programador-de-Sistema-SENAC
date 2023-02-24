import psycopg2

class Conexao:
    def __init__(self, parametroDB, parametroHost, parametroPort, parametroUser,parametroPassword):
        self._db = psycopg2.connect(database = parametroDB, host = parametroHost, port = parametroPort, user = parametroUser, password = parametroPassword)

    def consultarBanco(self, sql):
        cursor = self._db.cursor()

        cursor.execute(sql)

        resultado = cursor.fetchall()

        cursor.close()

        return resultado
    
    def manipularBanco(self, sql):

        cursor = self._db.cursor()

        cursor.execute(sql)

        self._db.commit()

        cursor.close()

        return True
    


    def fechar(self):
        self._db.close()