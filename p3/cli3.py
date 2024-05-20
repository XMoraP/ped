import os
import sys

fifo_p3 = '/tmp/fifo_p3'

if not os.path.exists(fifo_p3):
	os.mkfifo(fifo_p3)
#Abro la fifo
fifo_read = os.open('/tmp/fifo_p3', os.O_RDONLY)

#Ejemplo si tengo varios mensajes
try:
	while True:
		mensaje = os.read(fifo_read, 1024).decode('utf-8')
		if mensaje:	
			sys.stdout.write("Fecha y hora: " + mensaje + "\n")
		else:
			break
finally:
	os.close(fifo_read)


