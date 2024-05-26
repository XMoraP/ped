import unittest
from app.servidor import Servidor
from app.cliente import Cliente
from datetime import datetime

class Test(unittest.TestCase):
	def test_obtener_fecha(self):
		servidor = Servidor()
		fecha_actual = datetime.now().date().strftime("%d/%m/%Y")
		resultado = servidor.obtenerFecha()
		self.assertEqual(resultado, fecha_actual)
	
	def test_obtener_fecha_mal(self):
		servidor = Servidor()
		fecha_actual = "22/12/2020"
		resultado = servidor.obtenerFecha()
		self.assertTrue(resultado != fecha_actual)
	
	def test_obtener_hora(self):
		servidor = Servidor()
		hora_actual = datetime.now().time().strftime("%I:%M:%S %p")
		resultado = servidor.obtenerHora()
		self.assertEqual(resultado, hora_actual)

	def test_verificar_mensaje_cliente(self):
		servidor = Servidor()
		mensaje = "FECHA"
		resultado = servidor.verificarMensaje(mensaje)
		self.assertTrue(resultado)

if __name__ == '__main__':
	unittest.main()
