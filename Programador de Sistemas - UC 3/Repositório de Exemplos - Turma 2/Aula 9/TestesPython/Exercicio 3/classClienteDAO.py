import psycopg2
from classConexao import Conexao
from classCliente import Cliente

class ClienteDAO(Conexao):
    def __init__(self):
        super().__init__()
    
    def pegarClientePorId(self,idDoCliente):

        consultaCliente = self.consultarBanco(f'''
        SELECT * FROM "Clientes"
        WHERE "ID" = {idDoCliente}
        ''')

        if consultaCliente:
            novoCliente = Cliente(consultaCliente[0][1], consultaCliente[0][2])

            return novoCliente
        else:
            print("Ocorreu algum erro, talvez o cliente não exista.")
            return False
        
    def inserirNovoCliente(self,dadosDoCliente):

        resultado = self.manipularBanco(f'''
                            INSERT INTO "Clientes"
                            VALUES(default, '{dadosDoCliente[0]}', '{dadosDoCliente[1]}')
                            ''')
        
        if resultado:
            print("Inserção confirmada")
            return True
        else:
            print("Inserção falhou")
            return False
        

if __name__ == "__main__":
    cliente_dao = ClienteDAO()

    # cliente_dao.inserirNovoCliente(["José", 30])
    cliente = cliente_dao.pegarClientePorId(1)

    print(cliente.nome)