class Compra:
    def __init__(self, id, idCliente, idProduto, quantidade, valorTotal, timestamp):

        self._id = id
        self._idCliente = idCliente
        self._idProduto = idProduto
        self._quantidade = quantidade
        self._valorTotal = valorTotal
        self._timestamp = timestamp

    def sqlInserirCompra(self):

        sql = f'''
        INSERT INTO "Compras"
        VALUES(default, '{self._idCliente}', '{self._idProduto}', '{self._quantidade}', '{self._valorTotal}', default)
        
        '''

        return sql