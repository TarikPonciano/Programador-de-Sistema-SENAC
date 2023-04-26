class Cliente:
    def __init__(self,id,nome):
        self._id = id
        self._nome = nome

    def sqlInserirCliente(self):

        sql = f'''
        INSERT INTO "Clientes"
        Values(default, '{self._nome}')
        '''

        return sql