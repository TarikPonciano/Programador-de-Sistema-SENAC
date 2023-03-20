import unittest
import classFuncionario

class TestFuncionario(unittest.TestCase):
    def test_apresetar(self):

        funcionario = classFuncionario.Funcionario("João", 20)

        self.assertEqual("Olá meu nome é João e tenho 20 anos!", funcionario.apresentar())


if __name__ == "__main__":
    unittest.main()