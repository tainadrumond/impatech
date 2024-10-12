from lista import NumericalVector3D
import unittest

class TestNumericalVector3D(unittest.TestCase):
    def setUp(self):
        # Criação de vetores para os testes
        self.v1 = NumericalVector3D([1.0, 2.0, 3.0])
        self.v2 = NumericalVector3D([1.0, 2.0, 3.0])
        self.v3 = NumericalVector3D([1.0 + NumericalVector3D.epsilon / 2, 2.0, 3.0])
        self.v4 = NumericalVector3D([1.0 + 2 * NumericalVector3D.epsilon, 2.0, 3.0])
        self.v5 = NumericalVector3D([2.0, 3.0, 4.0])

    def test_equality(self):
        self.assertTrue(self.v1 == self.v2)  # Vetores iguais
        self.assertTrue(self.v1 == self.v3)  # Dentro da tolerância
        self.assertFalse(self.v1 == self.v4)  # Fora da tolerância

    def test_less_than(self):
        self.assertTrue(self.v1 < self.v5)  # v1 é menor que v5
        self.assertFalse(self.v5 < self.v1)  # v5 não é menor que v1

    def test_less_than_or_equal(self):
        self.assertTrue(self.v1 <= self.v2)  # v1 é igual a v2
        self.assertTrue(self.v1 <= self.v3)  # v1 é igual a v3 (dentro da tolerância)
        self.assertFalse(self.v4 <= self.v1)  # v4 não é menor ou igual a v1

    def test_greater_than(self):
        self.assertTrue(self.v5 > self.v1)  # v5 é maior que v1
        self.assertFalse(self.v1 > self.v5)  # v1 não é maior que v5

    def test_greater_than_or_equal(self):
        self.assertTrue(self.v2 >= self.v1)  # v2 é igual a v1
        self.assertTrue(self.v3 >= self.v1)  # v3 é igual a v1 (dentro da tolerância)
        self.assertFalse(self.v1 >= self.v4)  # v1 não é maior ou igual a v4

if __name__ == '__main__':
    unittest.main()