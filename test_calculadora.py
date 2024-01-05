import unittest
import calculadora

class TestCalculadora(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(calculadora.suma(3, 5), 8)
        self.assertEqual(calculadora.suma(-1, 1), 0)
        self.assertEqual(calculadora.suma(0, 0), 0)

    def test_resta(self):
        self.assertEqual(calculadora.resta(8, 3), 5)
        self.assertEqual(calculadora.resta(5, 5), 0)
        self.assertEqual(calculadora.resta(0, 0), 0)
        
    def test_multiplicacion(self):
        self.assertEqual(calculadora.multiplicacion(4, 6), 24)
        self.assertEqual(calculadora.multiplicacion(0, 10), 0)
        self.assertEqual(calculadora.multiplicacion(0, 0), 0)

    def test_division(self):
        self.assertEqual(calculadora.division(8, 2), 4)
        self.assertEqual(calculadora.division(8, 2), 8 / 2)
        with self.assertRaises(ValueError):
            calculadora.division(5, 0)

if __name__ == '__main__':
    unittest.main()
