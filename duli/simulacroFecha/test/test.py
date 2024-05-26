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

	def test_enviar_mensaje_fecha_cliente(self):
		cliente = Cliente()
		fecha = "FECHA"
		resultado = cliente.pedirFecha()
		self.assertEqual(fecha, resultado)

	def test_enviar_mensaje_hora_cliente(self):
		cliente = Cliente()
		hora = "HORA"
		resultado = cliente.pedirHora()
		self.assertEqual(hora, resultado)


		

if __name__ == '__main__':
	unittest.main()
