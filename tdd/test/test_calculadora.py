import unittest
from app.calculadora import Calculadora

class Test_calculadora(unittest.TestCase):
    def test_suma(self):
        calculadora = Calculadora()
        operacion = []
        operacion.append(2)
        operacion.append(2)
        suma = calculadora.suma(operacion)
        self.assertEqual(suma, 4)

    def test_diferencia(self):
         calculadora = Calculadora()
         operacion = [4,2]
         diferencia = calculadora.diferencia(operacion)
         self.assertEqual(diferencia, 2)
    
    def test_multiplicacion(self):
         calculadora = Calculadora()
         operacion = [8,100]
         multiplicar = calculadora.multiplicar(operacion)
         self.assertEqual(multiplicar, 800)
    
    def test_dividir(self):
         calculadora = Calculadora()
         operacion = [2,2]
         dividir = calculadora.dividir(operacion)
         self.assertEqual(dividir, 1)

if __name__ == '__main__':
	unittest.main()