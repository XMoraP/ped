import socket
from datetime import datetime

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serv_socket.bind(('0.0.0.0', 8000))
print("Servidor udp esperando clientes...")

try:
    while True:
            data, client_address = serv_socket.recvfrom(1024)
            print("Nueva conexión de cliente: ", client_address)
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            response = "Fecha y hora actual: " + current_time
            serv_socket.sendto(response.encode(), client_address)
except KeyboardInterrupt:
    print("Deteniendo el servidor...")
finally:
    serv_socket.close()
