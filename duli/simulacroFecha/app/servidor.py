from datetime import datetime
import socket
import os
import sys

class Servidor:
    def obtenerFecha(self):
        fecha_actual = datetime.now().date().strftime("%d/%m/%Y")
        return fecha_actual

    def obtenerHora(self):
        hora_actual = datetime.now().time().strftime("%I:%M:%S %p")
        return hora_actual

    def verificarMensaje(self, mensaje):
        if mensaje.lower() == "hora":
            return True
        elif mensaje.lower() == "fecha":
            return True
        else:
            return False

    def iniciar(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('0.0.0.0', 8000))
        server_socket.listen(3)
        print("Esperando clientes...")

        try:
            while True:
                connection, address = server_socket.accept()
                print(address)
                
                while True:
                    mensaje = connection.recv(1024).decode('utf-8').strip()
                    if self.verificarMensaje(mensaje):
                        if mensaje.lower() == "fecha":
                            connection.send(self.obtenerFecha().encode('utf-8'))
                        elif mensaje.lower() == "hora":
                            connection.send(self.obtenerHora().encode('utf-8'))
                    else:
                        error = "Petición inválida\n"
                        connection.send(error.encode('utf-8'))
        except BrokenPipeError:
            pass
        except KeyboardInterrupt:
            print("Server stopped")
        finally:
            server_socket.close()

if __name__ == '__main__':
    servidor = Servidor()
    servidor.iniciar()
