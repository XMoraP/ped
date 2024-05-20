class Partida:
    def conteoRondas(self, partida):
        resultado = len(partida)
        return resultado

    def tanteo(self, partida): 
        resultado = 0
        acumulador = 0
        i = 0        
        for ronda in partida:
            intentos = 2            
            for punto in ronda:
                if ronda is partida[9] and (ronda[0] == 10 or ronda[1] == 10 or (ronda[0] + ronda[1]) == 10) and len(ronda) is not 3:
                    raise ValueError("Falta Bonus")
                
                if len(ronda) == 3 and (ronda[0] < 10 and ronda[1] < 10 and (ronda[0] + ronda[1]) < 10):  
                    raise ValueError("No tienes mas tiros")
               
                if len(ronda) == 3 and ronda is partida[9] and ronda[0] + ronda[1] >= 10:
                        if (ronda [0] > 10) or (ronda [1] > 10) or (ronda [2] > 10): raise ValueError("Puntos invalidos")

                        if partida[i - 1] == [10,0]: 
                            acumulador = acumulador + (ronda[0] + ronda[1])

                        if ronda[2] == 10 and ronda[1] == 10 and ronda[0] == 10: 
                            resultado = resultado + (ronda[0] + ronda[1] + ronda[2]) 

                        elif ronda[0] == 10 and ronda[1] == 10:
                            resultado = resultado + (ronda[0] + ronda[1])

                        elif 0 < ronda[0] < 10 and ronda[1] == 10:
                            raise ValueError("Tiro no valido")
                        else:
                            resultado = resultado + (ronda[0] + ronda[1])                             

                        acumulador = acumulador + ronda[2]
                        break

                if partida[i - 2] == [10,0] and partida[i - 1] == [10,0] : acumulador = acumulador + punto
                if partida[i - 1] == [10,0]: 
                    acumulador = acumulador + punto

                if ((partida[i - 1][0] + partida[i - 1][1] == 10) and (partida[i - 1] != [10,0]) and (partida[i][0] is punto) and (i - 1) >= 0):
                    acumulador = acumulador + punto
                    
                if not isinstance(punto, int):
                   raise ValueError("Solo se aceptan numeros enteros")
                
                if punto < 0:
                    raise ValueError("No se aceptan numeros negativos")

                if intentos > 0 and punto <= 10:
                    if punto is partida[i][0]: 
                        if (partida[i][1] + punto) > 10 and ronda is not  partida[9]: 
                            raise ValueError("Solo hay diez bolos por ronda")
                        
                    resultado = resultado + punto
                    intentos = intentos - 1

            i = i + 1

        return (resultado + acumulador)