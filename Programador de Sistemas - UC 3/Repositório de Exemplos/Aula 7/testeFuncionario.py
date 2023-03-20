import unittest
import classFuncionario

class TestFuncionario(unittest.TestCase):
    def test_apresetar(self):

        funcionario = classFuncionario.Funcionario("João", 20)

        self.assertEqual(type(""), type(funcionario.apresentar()))


if __name__ == "__main__":
    unittest.main()