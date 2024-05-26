import datetime, socket
class Servidor:
	def get_hora(self):
		hora =  datetime.datetime.now().strftime("%H:%M:%S")
		return hora
	def get_fecha(self):
		fecha = datetime.datetime.now().strftime("%d/%m/%Y")
		return fecha
	def iniciar_servidor(self):
		socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		socket_servidor.bind(('0.0.0.0', 8000))
		
		while True:
			datos, addr = socket_servidor.recvfrom(512)
			if datos.decode('utf-8') == 'ok':	
				respuesta = self.get_fecha() + " " + self.get_hora()
				socket_servidor.sendto(respuesta.encode('utf-8'), addr)

if __name__ == "__main__":
	servidor = Servidor()
	servidor.iniciar_servidor()