class MarcadorBolos:
    def verificar_partida(self, partida):
        self.contarRondas(partida)
        for i in range(len(partida)):
            cuadro = partida[i]
            ultimo_cuadro = (i == len(partida) - 1)
            self.verificarRondasVacias(cuadro)
            self.verificarExcesoTiros(cuadro, ultimo_cuadro)
            self.verificarPuntosPorRonda(cuadro, ultimo_cuadro)
            self.verificarBonusInvalido(cuadro, ultimo_cuadro)
            self.verificarPuntosRondaBonus(cuadro, ultimo_cuadro)
            for tiro in cuadro:
                self.verificarTiroNegativo(tiro)
                self.verificarTiroDecimal(tiro)    
                          
    def contarRondas(self, partida):
        if len(partida) != 10:
            raise ValueError("Error: La partida no tiene 10 rondas")
        return True
    
    def verificarExcesoTiros(self, cuadro, ultimo_cuadro):
         if len(cuadro) > 2 and not ultimo_cuadro:
                raise ValueError("Error: Hay exceso de tiros en alguna ronda")
         if ultimo_cuadro and len(cuadro) > 3:
                raise ValueError("Error: Hay exceso de tiros en la última ronda")
        
    def verificarTiroNegativo(self, tiro):
        if tiro < 0:
            raise ValueError("Error: Los tiros no pueden ser negativos")
    def verificarTiroDecimal(self, tiro):
        if tiro != int(tiro):
            raise ValueError("Error: Los tiros no pueden ser decimales")
          
    def verificarPuntosPorRonda(self, cuadro, ultimo_cuadro):
        if any(isinstance(tiro, str) for tiro in cuadro):  
            raise ValueError("Error: Los tiros no pueden ser strings")
        if sum(cuadro) > 10 and not ultimo_cuadro:
            raise ValueError("Error: Los tiros no pueden sumar más de 10")
  
    def verificarRondasVacias(self, cuadro):
        if len(cuadro) == 0:
            raise ValueError("Error: El cuadro no puede estar vacío")
    
    def verificarBonusInvalido(self, cuadro, ultimo_cuadro):
        if cuadro[0] == 10 and ultimo_cuadro and len(cuadro) != 3:
            raise ValueError("Error: No se lanzaron los dos tiros extras luego del strike en la ronda final")
        elif sum(cuadro[0:2]) == 10 and ultimo_cuadro and len(cuadro) == 2:
            raise ValueError("Error: No se lanzó el tiro extra luego del spare en la ronda final")
        elif sum(cuadro[0:2]) < 10 and ultimo_cuadro and len(cuadro) == 3:
            raise ValueError("Error: Se lanzó el tiro extra sin haber hecho spare previamente en la ronda final")
        elif cuadro[0] < 10 and sum(cuadro[0:2]) > 10 and len(cuadro) == 3 and ultimo_cuadro:
            raise ValueError("Error: Los tiros no pueden sumar más de 10 en la última ronda sin bonus")
            
    def verificarPuntosRondaBonus(self, cuadro, ultimo_cuadro):
        if sum(cuadro) > 30 and len(cuadro) == 3 and ultimo_cuadro:
            raise ValueError("Error: Los tiros no pueden sumar más de 30 en la ronda final con bonus ")
        elif sum(cuadro) > 10 and len(cuadro) == 2 and ultimo_cuadro:
            raise ValueError("Error: Los tiros no pueden sumar más de 10 en la última ronda sin bonus")
            
#Métodos de calcular resultado del marcador
    def strike(self, cuadro):
        return cuadro[0] == 10 
    
    def spare(self, cuadro):
        return sum(cuadro) == 10
    
    def abierto(self,cuadro):
        return sum(cuadro) != 10
    
    def calcularPuntosStrike(self, i, partida):
        resultado = 10
        siguiente_cuadro = partida[i + 1]
        if len(siguiente_cuadro) == 1 and self.strike(siguiente_cuadro):
            if i + 2 < len(partida):
                siguiente_siguiente_cuadro = partida[i + 2]
                resultado += 10 + siguiente_siguiente_cuadro[0]
        elif len(siguiente_cuadro) == 3:
            resultado += siguiente_cuadro[0] + siguiente_cuadro[1]
        else:
            resultado += sum(siguiente_cuadro)
        return resultado

    def calcularPuntosSpare(self, i, partida):
        siguiente_cuadro = partida[i + 1]
        resultado = 10 + siguiente_cuadro[0]
        return resultado
    
    def calcularPuntosAbierto(self, cuadro):
        resultado = sum(cuadro)
        return resultado
    
    def calcularPuntosBonus(self, cuadro):
        resultado = sum(cuadro)
        return resultado
        
    def calcularResultado(self, partida):
        self.verificar_partida(partida)
        resultado = 0
        for i in range(len(partida)):
            cuadro = partida[i]
            if i == 9 and len(cuadro) == 3:
                resultado += self.calcularPuntosBonus(cuadro)
            else:    
                if self.strike(cuadro):
                    if i+1 < len(partida):
                        resultado += self.calcularPuntosStrike(i, partida)
                elif self.spare(cuadro):
                    if i+1 < len(partida):
                        resultado += self.calcularPuntosSpare(i, partida)
                elif self.abierto(cuadro):
                    resultado += self.calcularPuntosAbierto(cuadro) 
        return resultado

   
   
