from datetime import datetime, date, time, timedelta
import socket, os

class Cliente:
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = ('localhost', 8888)
    mensaje = "Hola soy el cliente"
    
    socket_cliente.sendto(mensaje.encode('utf-8'), address)

    data, _ = socket_cliente.recvfrom(1024)
    os.write(os.sys.stdout.fileno(), data)
    socket_cliente.close()
