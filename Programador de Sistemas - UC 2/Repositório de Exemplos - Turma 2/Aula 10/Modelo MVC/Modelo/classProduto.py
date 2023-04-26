class Produto:

    def __init__(self, id, nome, preço, estoque):
        self._id = id
        self._nome = nome
        self._preço = preço
        self._estoque = estoque

    def sqlInserirProduto(self):

        sql = f'''
        INSERT INTO "Produtos"
        VALUES(default, '{self._nome}', '{self._preço}', '{self._estoque}')
        
        '''

        return sql
    
    def sqlAtualizarProduto(self):

        sql = f'''
        UPDATE "Produtos"
        SET
        "Nome" = '{self._nome}', "Preço" = '{self._preço}', "Estoque" = '{self._estoque}'
        WHERE "Id" = {self._id}
        
        '''

        return sql