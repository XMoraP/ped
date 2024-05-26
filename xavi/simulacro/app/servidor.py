import datetime, socket

class Servidor:
	def get_hora_fecha(self, mensaje): 
		if mensaje.decode('utf-8') == 'HORA':
			hora = datetime.datetime.now().strftime("%H:%M:%S")
			return hora
		elif mensaje.decode('utf-8') == 'FECHA':
			fecha = datetime.datetime.now().strftime("%d/%m/%Y")
			return fecha
		else:
			return "Mensaje invalido"
	def iniciar_servidor(self): 
		socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket_servidor.bind(('0.0.0.0', 16082))
		socket_servidor.listen(3)
		while True: 
			socket_cliente, addr = socket_servidor.accept()
			try:
				while True:
					mensaje = socket_cliente.recv(512)
					respuesta = self.get_hora_fecha(mensaje)
					socket_cliente.send(respuesta.encode('utf-8'))
			except ConnectionResetError:
				pass

if __name__ == "__main__":
	servidor = Servidor()
	servidor.iniciar_servidor()