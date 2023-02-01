import psycopg2

class Conexao:
    
    def __init__(self, parametroDb, parametroHost, parametroPort, parametroUser, parametroPassword):
        self._db = psycopg2.connect(database = parametroDb, host = parametroHost, port = parametroPort, user = parametroUser, password = parametroPassword)

