from datetime import datetime
class Servidor:
	def obtenerFecha(self):
		fecha_actual = datetime.now().date().strftime("%d/%m/%Y")
		return fecha_actual

