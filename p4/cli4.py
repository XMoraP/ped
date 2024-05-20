import socket, os, sys

my_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
path = '/tmp/socket8'

file = sys.argv[1]

my_socket.connect(path)
fd = my_socket.fileno()

pid = os.getpid()
info = f"[{os.getpid()}]cli4: Conectado\n"
os.write(sys.stderr.fileno(), info.encode('utf-8'))

os.write(fd, file.encode('utf-8'))

try:
    while True:
        response = os.read(fd, 512)

        if not response:
            break

        os.write(sys.stdout.fileno(), response)
        
except KeyboardInterrupt:
    inf = f"[{os.getpid()}]cli4: ha sido interrumpido manualmente\n"
    os.write(sys.stderr.fileno(), inf.encode('utf-8'))

finally:
    os.close(fd)
