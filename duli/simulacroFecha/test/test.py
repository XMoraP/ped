import unittest
from app.servidor import Servidor

class Test(unittest.TestCase):
	def test(self):
		servidor = Servidor()
		ok = servidor.prueba()
		self.assertEqual(ok, 'ok')

if __name__ == '__main__':
	unittest.main()
