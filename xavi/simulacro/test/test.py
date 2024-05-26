import unittest, datetime
from app.servidor import Servidor

class Test(unittest.TestCase):
	def test_hora_servidor(self):
		servidor = Servidor()
		mensaje = 'HORA'
		respuesta = servidor.get_hora(mensaje.encode('utf-8'))
		hora = datetime.datetime.now().strftime("%H:%M:%S")
		self.assertEqual(hora, respuesta)
	def test_fecha_servidor(self):
		servidor = Servidor()
		mensaje = 'FECHA'
		respuesta = servidor.get_fecha(mensaje.encode('utf-8'))
		fecha = datetime.datetime.now().strftime("%d/%m/%Y")
		self.assertEqual(fecha, respuesta)

if __name__ == '__main__':
	unittest.main()
