import unittest
from main import checarPar

class TesteChecarPar(unittest.TestCase):

    def test_checarPar_dois(self):
        self.assertTrue(checarPar(2))

    def test_checarPar_cinco(self):
        self.assertFalse(checarPar(5))

    def test_checarPar_texto(self):
        self.assertRaises(TypeError, checarPar("Hello World"))

if __name__ == "__main__":
    unittest.main()