class Livro:
    def __init__(self, id, nome, autor):
        self._id = id
        self._nome = nome
        self._autor = autor
    
    def imprimirLivro(self):

        print(f'''
        ID - {self._id}
        Nome - {self._nome}
        Autor - {self._autor}
        ''')

    def consultarLivroPorID(self):
        sql = f'''
        SELECT * FROM "Livro"
        WHERE "ID" = '{self._id}'
        '''
        return sql

    def consultarAlugueis(self):
        sql = f'''
        SELECT * FROM "Aluguel"
        WHERE "ID_Livro" = '{self._id}'
        '''
        return sql

    def inserirLivro(self):
        sql = f'''
        INSERT INTO "Livro"
        VALUES(default, '{self._nome}', '{self._autor}')
        
        '''

        return sql