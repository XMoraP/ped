import unittest
from app.servidor import Servidor
from datetime import datetime, date, time, timedelta

class Test(unittest.TestCase):

	def test_fecha_hora(self):
		servidor = Servidor()
		resultado = servidor.obtenerFechaYhora()
		fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		self.assertEqual(fecha_hora, resultado)

if __name__ == '__main__':
	unittest.main()
