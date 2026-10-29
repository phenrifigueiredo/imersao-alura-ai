import unittest
from desafio_1_calculadora import somar, subtrair, multiplicar, dividir, potencia, porcentagem

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(somar(10, 5), 15)
        self.assertEqual(somar(-2, 5), 3)
        self.assertEqual(somar(0, 0), 0)

    def test_subtracao(self):
        self.assertEqual(subtrair(10, 5), 5)
        self.assertEqual(subtrair(5, 10), -5)
        self.assertEqual(subtrair(0, 5), -5)

    def test_multiplicacao(self):
        self.assertEqual(multiplicar(10, 5), 50)
        self.assertEqual(multiplicar(7, 0), 0)
        self.assertEqual(multiplicar(-3, 4), -12)

    def test_divisao(self):
        self.assertEqual(dividir(10, 2), 5.0)
        self.assertEqual(dividir(7, 2), 3.5)
        # Teste de divisão por zero: deve retornar None conforme a regra criada
        self.assertIsNone(dividir(10, 0))

    def test_potencia(self):
        self.assertEqual(potencia(2, 3), 8)
        self.assertEqual(potencia(5, 2), 25)
        self.assertEqual(potencia(9, 0), 1)

    def test_porcentagem(self):
        # 15% de 200 = 30.0
        self.assertEqual(porcentagem(200, 15), 30.0)
        # 50% de 80 = 40.0
        self.assertEqual(porcentagem(80, 50), 40.0)
        # 0% de 100 = 0.0
        self.assertEqual(porcentagem(100, 0), 0.0)

if __name__ == '__main__':
    unittest.main()
