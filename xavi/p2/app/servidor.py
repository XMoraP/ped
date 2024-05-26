import datetime, os

class Servidor:
	def get_hora(self): 
		hora = datetime.datetime.now().strftime("%H:%M:%S")
		return hora 
	def get_fecha(self):
		fecha = datetime.datetime.now().strftime("%d/%m/%Y")
		return fecha
	def iniciar_server(self):
		rd, wd = os.pipe()
		pid = os.fork() 
		if pid:
			os.close(rd)
			hora = self.get_hora()
			fecha = self.get_fecha()
			respuesta = fecha + " " + hora
			os.write(wd, respuesta.encode())
			os.close(wd)
		else:
			os.close(wd)
			res = os.read(rd, 512)
			print(res.decode())
			os.close(rd)
if __name__ == "__main__":
	servidor = Servidor()
	servidor.iniciar_server()