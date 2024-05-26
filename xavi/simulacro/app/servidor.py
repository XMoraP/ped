import datetime 

class Servidor:
	def get_hora_fecha(self, mensaje): 
		if mensaje.decode('utf-8') == 'HORA':
			hora = datetime.datetime.now().strftime("%H:%M:%S")
			return hora
		elif mensaje.decode('utf-8') == 'FECHA':
			fecha = datetime.datetime.now().strftime("%d/%m/%Y")
			return fecha
		else:
			raise ValueError("ERROR")