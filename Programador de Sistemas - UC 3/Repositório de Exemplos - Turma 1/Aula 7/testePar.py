import unittest
import par

class TestPar(unittest.TestCase):
    def test_checar_par_true(self):

        self.assertEqual("É par",par.checarPar(2), "Ocorreu um erro")

        self.assertEqual("É par",par.checarPar(100), "Ocorreu um erro")

        self.assertEqual("É par",par.checarPar(200), "Ocorreu um erro")

        self.assertEqual("É par",par.checarPar(252), "Ocorreu um erro")

    def test_checar_par_false(self):

        self.assertEqual("É impar",par.checarPar(3),"Ocorreu um erro")
        self.assertEqual("É impar",par.checarPar(7),"Ocorreu um erro")
        self.assertEqual("É impar",par.checarPar(11),"Ocorreu um erro")
        self.assertEqual("É impar",par.checarPar(-3),"Ocorreu um erro")

    def test_checar_par_error(self):

        self.assertRaises(TypeError, par.checarPar,2, "Não ocorreu erro de tipagem")

if __name__ == "__main__":
    unittest.main()