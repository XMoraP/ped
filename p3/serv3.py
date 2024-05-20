import os
import time
from datetime import datetime

fifo = '/tmp/fifo_p3'

if not os.path.exists(fifo):
	os.mkfifo(fifo)

fifo_write = os.open(fifo, os.O_WRONLY)
try:
#Ejemplo para mandar varios mensajes
	while True:
		try:
			mensaje = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			os.write(fifo_write, mensaje.encode('utf-8'))

		except BrokenPipeError:
			print("Esperando nuevos clientes....")
			os.close(fifo_write)
			fifo_write = os.open(fifo, os.O_WRONLY)
		except Exception as e:
			print("Error", e)
		finally:
			time.sleep(0.1)
finally:
	os.close(fifo_write)