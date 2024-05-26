import unittest
from app.servidor import Servidor
from datetime import datetime

class Test(unittest.TestCase):
	def test_obtener_fecha(self):
		servidor = Servidor()
		fecha_actual = datetime.now().date().strftime("%d/%m/%Y")
		resultado = servidor.obtenerFecha()
		self.assertEqual(resultado, fecha_actual)
		

if __name__ == '__main__':
	unittest.main()
