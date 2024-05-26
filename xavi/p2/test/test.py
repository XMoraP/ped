import unittest
import datetime
from app.servidor import Servidor

class Test(unittest.TestCase):
	def test_get_hora(self):
		servidor = Servidor()
		result = servidor.get_hora()
		hora = datetime.datetime.now().strftime("%H:%M:%S")
		self.assertEqual(hora, result)
	def test_get_fecha(self):
		servidor = Servidor()
		result = servidor.get_fecha()
		fecha = datetime.datetime.now().strftime("%d/%m/%Y")
		self.assertEqual(fecha, result)

if __name__ == '__main__':
	unittest.main()
