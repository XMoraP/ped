import unittest
from aplicacion.kata import partida_bolos

class TestCalcularResultado(unittest.TestCase):
    partida_bolos_instance = partida_bolos()

    def test_partida_valida_10_rondas(self):
        partida_bolos_lista = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]] 
        self.assertTrue(self.partida_bolos_instance.contar_el_round(partida_bolos_lista) == 10)  

    def test_todos_strike(self):
        resultado = self.partida_bolos_instance.todos_strike()
        self.assertEqual(resultado, 300)

if __name__ == '__main__':
    unittest.main()
