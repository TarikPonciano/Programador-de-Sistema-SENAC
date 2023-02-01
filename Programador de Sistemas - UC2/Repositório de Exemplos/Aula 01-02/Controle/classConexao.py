import psycopg2

class Conexao:
    
    def __init__(self, parametroDb, parametroHost, parametroPort, parametroUser, parametroPassword):
        self._db = psycopg2.connect(database = parametroDb, host = parametroHost, port = parametroPort, user = parametroUser, password = parametroPassword)

    def consultarBanco(self,sql):
        cursor = self._db.cursor()

        cursor.execute(sql)

        resultado = cursor.fetchall()

        cursor.close()

        return resultado

    def manipularBanco(self):
        #Criar cursor
        #Executar o sql que vem do parâmetro
        #Fazer o commit da conexão
        #Fechar o cursor
