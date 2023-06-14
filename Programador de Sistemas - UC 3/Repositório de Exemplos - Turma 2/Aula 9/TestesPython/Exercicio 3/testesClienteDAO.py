from classClienteDAO import ClienteDAO
import unittest

class TesteClienteDAO(unittest.TestCase):

    def test_metodo_inserir(self):
        cliente_dao = ClienteDAO()

        self.assertTrue(cliente_dao.inserirNovoCliente(["Paulin", 50]))

    def test_metodo_inserir_completo(self):
        cliente_dao = ClienteDAO()
        cliente = ["João", 26]

        cliente_dao.inserirNovoCliente(cliente)

        consultaCliente = cliente_dao.consultarBanco(f'''SELECT * FROM "Clientes"
            WHERE "Nome" = '{cliente[0]}' ''')
        
        self.assertTrue(consultaCliente)




if __name__ == "__main__":
    unittest.main()