from datetime import datetime
class Servidor:
	def obtenerFecha(self):
		fecha_actual = datetime.now().date().strftime("%d/%m/%Y")
		return fecha_actual

	def obtenerHora(self):
		hora_actual = datetime.now().time().strftime("%I:%M:%S %p")
		return hora_actual

