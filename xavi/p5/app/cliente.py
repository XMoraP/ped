import socket

class cliente:
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = (('localhost', 8000))
    mensaje = 'ok'
    socket_cliente.sendto(mensaje.encode('utf-8'), addr)
    datos, _ = socket_cliente.recvfrom(512)
    print(datos.decode('utf-8'))
    socket_cliente.close