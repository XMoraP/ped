import os, sys
from datetime import datetime, date, time, timedelta

class Servidor:
	def obtenerFechaYhora(self):
		resultado = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		return resultado

	def iniciar(self):
		rd, wd = os.pipe()
		pid = os.fork()

		if pid: #padre
			os.close(rd)
			mensaje = self.obtenerFechaYhora()
			os.write(wd, mensaje.encode('utf-8'))
			os.close(wd)
			os.wait()
		else:
			os.close(wd)
			mensaje = os.read(rd, 1024).decode('utf-8')
			print(mensaje)
			os.close(rd)

if __name__ == '__main__':
	servidor = Servidor()
	servidor.iniciar()

	





