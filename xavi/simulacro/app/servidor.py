import datetime 

class Servidor:
	def get_hora(self, mensaje): 
		if mensaje.decode('utf-8') == 'HORA':
			hora = datetime.datetime.now().strftime("%H:%M:%S")
			return hora
	def get_fecha(self, mensaje):
		return 'ok'

