import socket
import select
import sys
import getpass

sys.path.append('/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages')
from passlib.context import CryptContext

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect(('localhost', 8888))

context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=50000
)

def user_name():
    if sys.argv[1] == 'no':
        user_name = sys.argv[2]
        return user_name
    else:
        user_name = sys.argv[1]
        return user_name

def auth():
    if sys.argv[1] == 'no':
        user_name = sys.argv[2]
        passwd = getpass.getpass(prompt="Introduzca su contraseña: ")
        hashed_password = context.hash(passwd)
        print(f"Contraseña ingresada: {passwd}")
        print(f"Contraseña encriptada: {hashed_password}")
        cliente_socket.send(user_name.encode())
        cliente_socket.recv(1024).decode()
        validar = 'no ok'
        cliente_socket.send(validar.encode())
        cliente_socket.recv(1024).decode()
        cliente_socket.send(hashed_password.encode())
        print(cliente_socket.recv(1024).decode())
        print(cliente_socket.recv(1024).decode())
        pass
    else:
        user_name = sys.argv[1]
        cliente_socket.send(user_name.encode())
        cliente_socket.recv(1024).decode()
        validar = 'ok'
        cliente_socket.send(validar.encode())
        if cliente_socket.recv(1024).decode().strip().startswith('ok'):
            passwd = getpass.getpass(prompt="Introduzca su contraseña: ")
            cliente_socket.send(passwd.encode())
        else:
            print('Nombre de usuario no valido')
            sys.exit()


new_user = f'[' + str(user_name()) + ']'

lista_lectura = [cliente_socket, sys.stdin]
lista_conexiones = [cliente_socket, sys.stdin]

def mostrar_prompt():
    # Imprime el prompt sin nueva línea al final.
    print(f'[{str(user_name())}]: ', end=' ', flush=True)


auth()
while True:
    lectura, _, _ = select.select(lista_lectura, [], [])
    
    for sock in lectura:
        if sock is cliente_socket:
            mensaje = cliente_socket.recv(1024).decode()
            if not mensaje:
                print("Desconectando...")
                sys.exit()
            else: 
                print(f'\r{mensaje}')
        else:
            mensaje = input().strip()
            cliente_socket.send(mensaje.encode())
            mostrar_prompt()


cliente_socket.close()

