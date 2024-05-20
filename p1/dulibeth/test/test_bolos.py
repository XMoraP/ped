import unittest
from bolos.bolos import MarcadorBolos

bolos = MarcadorBolos()
class testBolos(unittest.TestCase):
    def test_partida_10_rondas(self):   
        partida = [[0],[0], [0], [0], [0], [0], [0], [0], [0], [0]]  
        self.assertTrue(bolos.contarRondas(partida))

    def test_partida_11_rondas(self):   
        partida_11_rondas = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]  
        with self.assertRaises(ValueError):
            bolos.verificar_partida(partida_11_rondas)

    def test_partidas_con_rondas_vacías(self):
        partida_vacia = [[], [], [], [], [], [], [], [], [], []]  
        with self.assertRaises(ValueError):
            bolos.verificar_partida(partida_vacia)
    
    def test_partida_string(self):
        partida_string= [['a'],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
        with self.assertRaises(ValueError):
            bolos.verificar_partida(partida_string)
              
    def test_partida_numeros_negativos(self):
        partida_negativo = [[-10],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
        with self.assertRaises(ValueError):
            bolos.verificar_partida(partida_negativo)
    
    def test_partida_numeros_decimales(self):
        partida_decimal = [[1.1, 2],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
        with self.assertRaises(ValueError):
            bolos.verificar_partida(partida_decimal)

    def test_maximo_diez_puntos_por_ronda(self):
        partida = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[8,6]]
        with self.assertRaises(ValueError):
            bolos.verificar_partida(partida)

    def test_maximo_treinta_puntos_bonus(self):
        partida_bonus = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[10,10,15]]
        with self.assertRaises(ValueError):
            bolos.verificar_partida(partida_bonus)

    def test_maximo_dos_tiros_por_ronda(self):
        partida = [[6, 4, 6],[4, 3],[7, 2],[5, 4],[8, 1],[9, 0],[10],[7, 3],[6, 3],[10, 8]]
        with self.assertRaises(ValueError):
            bolos.verificar_partida(partida)
    
    def test_tres_tiros_ultima_ronda(self):
        partida = [[10],[4, 3],[7, 2],[5, 4],[8, 1],[9, 0],[10],[7, 3],[6, 3],[10, 8, 1]]
        try:
            bolos.verificar_partida(partida)
        except ValueError:
            self.fail("Se lanzó una excepción para una partida que si es válida")

    def test_es_strike(self):
       cuadro = [10]
       resultado = bolos.strike(cuadro)
       self.assertTrue(resultado)

    def test_es_spare(self):
       cuadro = [7,3]
       resultado = bolos.spare(cuadro)
       self.assertTrue(resultado)
    
    def test_es_abierto(self):
        cuadro = [6,2]
        resultado = bolos.abierto(cuadro)
        self.assertTrue(resultado)

    def test_calcular_puntos_abierto(self):
        cuadro = [6,2]
        resultado = bolos.calcularPuntosAbierto(cuadro)
        self.assertEqual(8, resultado)

    def test_calcular_puntos_un_strike(self):
        partida_strike = [[10], [6,3], [0], [0], [0], [0], [0], [0], [0], [0]]
        resultado = bolos.calcularResultado(partida_strike)
        self.assertEqual(28, resultado)

    def test_calcular_puntos_un_spare(self):
        partida_spare = [[6,4], [6,3], [0], [0], [0], [0], [0], [0], [0], [0]]
        resultado = bolos.calcularResultado(partida_spare)
        self.assertEqual(25, resultado)

    def test_sin_strike_ni_spare(self):
        partida = [[7,2], [6,3], [0], [0], [0], [0], [0], [0], [0], [0]]
        resultado = bolos.calcularResultado(partida)
        self.assertEqual(18, resultado)    

    def test_dos_strikes(self):
        partida = [[10], [10], [6,3], [0], [0], [0], [0], [0], [0], [0]]
        resultado = bolos.calcularResultado(partida)
        self.assertEqual(54, resultado)
    
    def test_tres_strikes(self):
        partida_spare = [[10], [10], [10], [0], [0], [0], [0], [0], [0], [0]]
        resultado = bolos.calcularResultado(partida_spare)
        self.assertEqual(60, resultado)

    def test_calcular_puntos_tiro_bonus(self):
        cuadro_bonus =  [10, 6, 2]
        resultado = bolos.calcularPuntosBonus(cuadro_bonus)
        self.assertEqual(18, resultado)

    def test_partida_con_bonus_strike(self):
         partida = [[10],[0],[0],[0],[0],[0],[0],[0],[0],[10, 8, 1]]
         resultado = bolos.calcularResultado(partida)
         self.assertEqual(29, resultado)
    
    def test_partida_perfecta_solo_strikes_y_bonus(self):
         partida_perfecta = [[10], [10], [10], [10], [10], [10], [10], [10], [10], [10,10,10]]
         resultado = bolos.calcularResultado(partida_perfecta)
         self.assertEqual(300, resultado)

    def test_partida_perfecta_con_bonus_spare(self):
        partida= [[10], [10], [10], [10], [10], [10], [10], [10], [10], [6,4,1]]
        resultado = bolos.calcularResultado(partida)
        self.assertEqual(267, resultado)
        
    def test_partida_mixta_spare_strike_abierto(self):
        partida_mixta = [[10], [7, 3], [6, 2], [10], [0, 10], [8, 1], [4, 5], [10], [5, 5], [10, 10, 10]]
        resultado = bolos.calcularResultado(partida_mixta)
        self.assertEqual(170, resultado)
    
    def test_partida_solo_tiros_abiertos(self):
        partida_abierta = [[2, 3], [4, 1], [5, 2], [3, 2], [2, 3], [4, 5], [1, 4], [3, 1], [2, 2], [4, 1]]
        resultado = bolos.calcularResultado(partida_abierta)
        self.assertEqual(54, resultado)
    
    def test_partida_solo_ceros(self):
        partida_ceros = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
        resultado = bolos.calcularResultado(partida_ceros)
        self.assertEqual(0, resultado)
    
    def test_partida_solo_spare(self):
        partida_spares = [[5, 5], [6, 4], [3, 7], [8, 2], [9, 1], [2, 8], [4, 6], [7, 3], [1, 9], [5, 5, 5]]
        resultado = bolos.calcularResultado(partida_spares)
        self.assertEqual(150, resultado)

    def test_partida_con_bonus_incompleto_strike(self):
        partida_bonus_incompleto = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [10]]
        with self.assertRaises(ValueError):
            bolos.verificar_partida(partida_bonus_incompleto)
    
    def test_partida_con_bonus_incompleto_strike_un_tiro(self):
        partida_bonus_un_tiro = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [10, 5]]
        with self.assertRaises(ValueError):
            bolos.verificar_partida(partida_bonus_un_tiro)
    
    def test_partida_con_bonus_incompleto_spare(self):
        partida_bonus_incompleto = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [5,5]]
        with self.assertRaises(ValueError):
            bolos.verificar_partida(partida_bonus_incompleto)
    
    def test_partida_sin_bonus_con_bonus(self):
        partida_sin_bonus = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [5, 4, 10]]
        with self.assertRaises(ValueError):
            bolos.verificar_partida(partida_sin_bonus)

if __name__ == '__main__':
    unittest.main()