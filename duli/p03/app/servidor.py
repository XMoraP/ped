from datetime import datetime, date, time, timedelta
import socket, os

class Servidor:
	def obtenerFechaYhora(self):
		resultado = datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")
		return resultado

	def iniciar(self):
		servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		servidor_socket.bind(('0.0.0.0', 8888))
		datos, address = servidor_socket.recvfrom(1024)
		print("Cliente conectado", address)
		mensaje = self.obtenerFechaYhora()
		servidor_socket.sendto(mensaje.encode('utf-8'), address)
		servidor_socket.close()

if __name__ == '__main__':
	servidor = Servidor()
	servidor.iniciar()
