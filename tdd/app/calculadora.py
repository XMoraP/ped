class Calculadora:
    def suma(self, operacion):
        result = operacion[0] + operacion[1]
        return result

    def diferencia(self, operacion):
        result = operacion[0] - operacion[1]
        return result
    
    def multiplicar(self, operacion):
        result = operacion[0] * operacion[1]
        return result

    def dividir(self, operacion):
        result = operacion[0] / operacion[1]
        return result