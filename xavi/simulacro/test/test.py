import unittest, datetime
from app.servidor import Servidor

class Test(unittest.TestCase):
	def test_hora_servidor(self):
		servidor = Servidor()
		mensaje = 'HORA'
		respuesta = servidor.get_hora(mensaje.encode('utf-8'))
		hora = datetime.datetime.now().strftime("%H:%M:%S")
		self.assertEqual(hora, respuesta)

if __name__ == '__main__':
	unittest.main()
