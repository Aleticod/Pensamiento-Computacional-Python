import unittest


def es_mayor_edad(edad):
    if edad >= 18:
        return True
    else:
        return False


class UnitTestCristal(unittest.TestCase):
    def test_es_mayor(self):
        edad = 20
        resultado = es_mayor_edad(edad)

        self.assertEqual(resultado, True)


    def test_es_menor(self):
        edad = 10
        resultado = es_mayor_edad(edad)

        self.assertEqual(resultado, False)



if __name__ == '__main__':
    unittest.main(verbosity = 5)
