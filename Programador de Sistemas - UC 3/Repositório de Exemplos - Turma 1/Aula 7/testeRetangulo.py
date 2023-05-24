import classRetangulo
import unittest
from unittest.mock import patch, call
import sys

class TestRetangulo(unittest.TestCase):

    def test_area(self):

        retangulo = classRetangulo.Retangulo(2,2)
        self.assertEqual(4,retangulo.area())

    @patch('builtins.print')
    def test_informacoes(self,mocked_print):
        retangulo = classRetangulo.Retangulo(2,2)
        retangulo.informacoes()
        self.assertEqual([call('Teste 2 2')], mocked_print.mock_calls)
        

if __name__ == "__main__":
    unittest.main()