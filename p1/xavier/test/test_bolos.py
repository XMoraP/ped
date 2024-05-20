import unittest
from aplicacion.bolos import Partida

partida = Partida()

class TestBolos(unittest.TestCase):
    def testNumeroRondas(self):
        resultadoPartida = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
        resultadoRondas = partida.conteoRondas(resultadoPartida)
        self.assertEqual(resultadoRondas, 10)

    def testPartida(self):
        resultadoPartida = [[1,0], [0,0], [0,5], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
        tanteo = partida.tanteo(resultadoPartida)
        self.assertEqual(tanteo, 6)
    
    def testPartidaNumNegativo(self):
        resultadoPartidaNumNegativo = [[1,0], [0,0], [0,5], [0,0], [0,0], [0,0], [-1,0], [0,0], [0,0], [0,0]]
        
        with self.assertRaises(ValueError):        
            partida.tanteo(resultadoPartidaNumNegativo)
    
    def testPartidaString(self):
        resultadoPartidaString = [[1,0], [0,0], [0,5], [0,0], [0,0], [0,0], ["nueve",0], [0,0], [0,0], [0,0]]
        with self.assertRaises(ValueError):
            partida.tanteo(resultadoPartidaString) 
    
    def testFloat(self):
        resultadoPartidaFloat = [[1,0], [0,0], [0,5], [0,0], [0,0], [0,0], [7.7,0], [0,0], [0,0], [0,0]]
        with self.assertRaises(ValueError):
            partida.tanteo(resultadoPartidaFloat) 
    
    def testCaracterEspecial(self):
        resultadoPartidaCrtEspecial = [[1,0], [0,0], [0,5], [0,0], [0,0], [0,0], ['$',0], [0,0], [0,0], [0,0]]
        with self.assertRaises(ValueError):
            partida.tanteo(resultadoPartidaCrtEspecial) 
    
    def testTiradaMayorDiez(self):
        resultadoPartidaMayorDiez = [[1,0], [0,0], [0,5], [0,0], [0,0], [0,0], [12,0], [0,0], [0,0], [0,0]]
        tanteo = partida.tanteo(resultadoPartidaMayorDiez)
        self.assertEqual(tanteo, 6)
	
    def testPartidaConUnStrike(self):
        resultadoPartidaConUnStrike = [[10,0], [0,9], [6,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
        tanteo = partida.tanteo(resultadoPartidaConUnStrike)
        self.assertEqual(tanteo, 34)
    
    def testPartidaConDosStrikes(self):
        resultadoPartidaConDosStrikes = [[10,0], [10,0], [5,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
        tanteo = partida.tanteo(resultadoPartidaConDosStrikes)
        self.assertEqual(tanteo, 45)
    
    def testPartidaConTresStrikes(self):
        resultadoPartidaConTresStrike = [[10,0], [10,0], [10,0], [8,0], [4,3], [0,5], [4,2], [1,3], [3,2], [6,0]]
        tanteo = partida.tanteo(resultadoPartidaConTresStrike)
        self.assertEqual(tanteo, 117)

    def testPartidaConUnSpare(self):
        resultadoPartidaConUnSpare = [[10,0], [0,9], [6,4], [1,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
        tanteo = partida.tanteo(resultadoPartidaConUnSpare)
        self.assertEqual(tanteo, 40)

    def testPartidaConDosSpares(self):
            resultadoPartidaConDosSpares = [[10,0], [0,9], [6,4], [1,9], [1,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
            tanteo = partida.tanteo(resultadoPartidaConDosSpares)
            self.assertEqual(tanteo, 51)
    def testPartidaContresSpares(self):
            resultadoPartidaConTresSpares = [[10,0], [0,9], [6,4], [1,9], [8,2], [0,1], [0,0], [0,0], [0,0], [0,0]]
            tanteo = partida.tanteo(resultadoPartidaConTresSpares)
            self.assertEqual(tanteo, 68)

    def testRondaAbierta(self):
        resultadoRondaAbierta = [[1,2], [3,4], [5,2], [2,4], [1,3], [0,0], [0,0], [0,0], [0,0], [0,0]]
        tanteo = partida.tanteo(resultadoRondaAbierta)
        self.assertEqual(tanteo, 27)

    def testSumaDosTiradasMayorDiez(self):
        resultadoPartidaDosTiradasMayorDiez = [[1,2], [3,4], [5,3], [2,4], [1,3], [5,8], [0,0], [5,7], [0,0], [0,0]]
        with self.assertRaises(ValueError):
            partida.tanteo(resultadoPartidaDosTiradasMayorDiez)

    def testPartidaConBonusSpare(self):
        resultadoPartidaConBonusSpare = [[10,0], [10,0], [8,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [5,5,1]]
        tanteo = partida.tanteo(resultadoPartidaConBonusSpare)
        self.assertEqual(tanteo, 65)   

    def testPartidaConBonusStrike(self):
        resultadoPartidaConBonusStrike = [[10,0], [10,0], [8,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [10,10,1]]
        tanteo = partida.tanteo(resultadoPartidaConBonusStrike)
        self.assertEqual(tanteo, 75)
    
    def testPartidaConBonusNumMayorDiez(self):
        resultadoPartidaConBonusNumMayorDiez = [[10,0], [10,0], [8,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [10,11,1]]
        with self.assertRaises(ValueError):
            partida.tanteo(resultadoPartidaConBonusNumMayorDiez)

    def testPartidaConStrikeAntesBonus(self):
        resultadoPartidaConStrikeAntesBonus = [[10,0], [10,0], [8,0], [0,0], [0,0], [0,0], [0,0], [0,0], [10,0], [10,10,1]]
        tanteo = partida.tanteo(resultadoPartidaConStrikeAntesBonus)
        self.assertEqual(tanteo, 105)  
    
    def testJuegoPerfecto(self):
        resultadoPartidaJuegoPerfecto = [[10,0], [10,0], [10,0], [10,0], [10,0], [10,0], [10,0], [10,0], [10,0], [10,10,10]]
        tanteo = partida.tanteo(resultadoPartidaJuegoPerfecto)
        self.assertEqual(tanteo, 300)
    
    def testPartidaStrikeFaltaBonus(self):
        resultadoPartidaStrikeFaltaBonus = [[10,0], [10,0], [8,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [10,10]]
        with self.assertRaises(ValueError):
            partida.tanteo(resultadoPartidaStrikeFaltaBonus)

    def testPartidaSpareFaltaBonus(self):
        resultadoPartidaSpareFaltaBonus = [[10,0], [10,0], [8,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [3,7]]
        with self.assertRaises(ValueError):
            partida.tanteo(resultadoPartidaSpareFaltaBonus)
    
    def testPartidaConBonusFalso(self):
        resultadoPartidaConBonusFalso = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [3,3,3]]
        with self.assertRaises(ValueError):
            partida.tanteo(resultadoPartidaConBonusFalso)
    
    # Ronda final con strike en la segunda tirada
    def testPartidaRondaFinal(self):
        resultadoPartidaRondaFinal =  [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [1,10,1]]
        with self.assertRaises(ValueError):
            partida.tanteo(resultadoPartidaRondaFinal)
        
    def testRondaConDosStrikes(self):
        resultadoRondaConDosStrikes =  [[10,10], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [1,9,1]]
        with self.assertRaises(ValueError):
            partida.tanteo(resultadoRondaConDosStrikes)
    
    # Test spare en ronda final: primera tirada 0 y segunda tirada 10
    def testRondaFinal(self):
        resultadoRondaFinal =  [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,10,1]]
        tanteo = partida.tanteo(resultadoRondaFinal)
        self.assertEqual(tanteo, 11)

if __name__ == '__main__':
	unittest.main()
