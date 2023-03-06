class Cliente:
    def __init__(self, id, nome, cpf):
        self._id = id
        self._nome = nome
        self._cpf = cpf
    
    def imprimirCliente(self):

        print(f'''
        ID - {self._id}
        Nome - {self._nome}
        CPF - {self._cpf}
        ''')

    def consultarClientePorID(self):
        sql = f'''
        SELECT * FROM "Cliente"
        WHERE "ID" = '{self._id}'
        '''
        return sql

    def consultarAlugueis(self):
        sql = f'''
        SELECT * FROM "Aluguel"
        WHERE "ID_Cliente" = '{self._id}'
        '''
        return sql

    def inserirCliente(self):
        sql = f'''
        INSERT INTO "Cliente"
        VALUES(default, '{self._nome}', '{self._cpf}')
        
        '''

        return sql