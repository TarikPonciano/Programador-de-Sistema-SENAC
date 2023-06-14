import unittest
from classFuncionario import Funcionario

class TesteFuncionario(unittest.TestCase):
    def test_metodo_apresentar(self):
        nomeFuncionario = "Manoel"
        idadeFuncionario = 25

        novoFuncionario = Funcionario(nomeFuncionario, idadeFuncionario)

        self.assertEqual(novoFuncionario.apresentar(), "Olá meu nome é Manoel e tenho 25 anos", "Houve um erro no método apresentar()")

if __name__ == "__main__":
    unittest.main()