import socket, os, sys

path = '/tmp/socket8'
my_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
my_socket.bind(path)

my_socket.listen(2)
pid = os.getpid()

try:
    while True: 
        
        connection, addr = my_socket.accept()

        info = f"[{os.getpid()}]serv4: Nueva conexion\n"
        os.write(sys.stderr.fileno(), info.encode('utf-8'))
        
        fd = connection.fileno()

        file_bytes = os.read(fd, 512)
        file = file_bytes.decode('utf-8')
        
        try:
            content = os.open(file, os.O_RDONLY)
            while True:
                data = os.read(content, 512)
                if not data:
                    break
                os.write(fd, data)
            os.close(content)
            connection.close()

        except FileNotFoundError:
            inf = f"El fichero no existe"
            os.write(fd, inf.encode('utf-8'))
        except BrokenPipeError:
            pass
        
        connection.close()
        

except  KeyboardInterrupt:
    inf = f"[{os.getpid()}]serv4: ha sido interrumpido manualmente\n"
    os.write(sys.stderr.fileno(), inf.encode('utf-8'))

finally:
    my_socket.close()
    os.unlink(path)

