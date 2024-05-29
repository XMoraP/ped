import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(5)
try:
    data = 'Hola soy el cliente'
    client_socket.sendto(data.encode(), ('192.168.127.138', 8000))
    response, server_address = client_socket.recvfrom(1024)

    print(response.decode())
except socket.timeout:
    print("Tiempo de espera agotado. No se recibió respuesta del servidor.")
except KeyboardInterrupt:
    pass
finally:
    client_socket.close()
