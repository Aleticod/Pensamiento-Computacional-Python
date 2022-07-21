import unittest # Es un modulo de python que nos permite generar pruebas

def suma(numero_1: int, numero_2: int):
    return numero_1 + numero_2


class UnitTest(unittest.TestCase):
    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5
        resultado = suma(num_1, num_2)
        self.assertEqual(resultado, 15)
    
    
    def test_suma_dos_negativos(self):
        num_1 = -2
        num_2 = -59
        resultado = suma(num_1, num_2)
        self.assertEqual(resultado, -61)

if __name__ == '__main__':
    unittest.main()

