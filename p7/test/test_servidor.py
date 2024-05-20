import unittest
import sys
from app.serv7 import Server
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages')
from passlib.context import CryptContext

context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=50000
)
server = Server()
class test_server(unittest.TestCase):

    def test_verificar_credenciales(self):
        user_name = '[usuario1]'
        passwd = 'passwd'
        otra_passwd = 'otra_passwd'
        hashed_password = context.hash(passwd)
        hashed_otra_password = context.hash(otra_passwd)
        server.registro(user_name, hashed_password)
        result = server.verificar_credenciales(user_name, hashed_otra_password)
        self.assertEqual(result, 'Contraseña incorrecta')

    def test_registrar_usuario_exito(self):
        user_name = '[usuario1]'
        passwd = 'passwd'
        hashed_password = context.hash(passwd)
        result = server.registro(user_name, hashed_password)
        self.assertEqual(result, '\nBienvenid@ nuevo usuario')

    def test_registro_username(self):
        user_name = '[usuario1]'
        passwd = 'passwd'
        hashed_password = context.hash(passwd)
        server.registro(user_name, hashed_password)
        result = server.bd_usuarios[user_name]['name']
        self.assertEqual(result, user_name)

if __name__ == '__main__':
    unittest.main()