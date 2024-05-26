import socket, os, sys 
class Cliente:
    servidor = input("Ingrese la dirección del servidor (e.g., 'localhost'): ")   
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((servidor,8000))
    print("Conexion realizada")


    for _ in range(3):
        while True:
            peticion = input("Ingrese peticion: ")
            client_socket.send(peticion.encode('utf-8'))
            respuesta = client_socket.recv(1024).decode()
            print(respuesta)
            break
    client_socket.close()

    
