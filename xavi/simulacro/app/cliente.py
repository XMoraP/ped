import socket

class Cliente:
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = input("Introduzca la direcccion: ")
    socket_cliente.connect((addr, 16082))
    i = 0
    while i <= 2:
        mensaje = input("¿Que quieres?: ")
        socket_cliente.send(mensaje.encode())
        respuesta = socket_cliente.recv(512)
        print(respuesta.decode('utf-8'))
        i += 1
    socket_cliente.close()
