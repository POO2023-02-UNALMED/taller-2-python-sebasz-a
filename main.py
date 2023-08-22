class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        n = 0  #contador de objetos Asiento en la lista asientos
        for i in self.asientos:
            if i != None:
                n+= 1
        return n
    
    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for i in self.asientos:
                if i != None:
                    if i.registro != self.registro:
                        return "Las piezas no son originales"
        return "Auto original"
        
class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color in ["rojo", "negro", "amarillo", "verde", "blanco", "negro"]:
            self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo in ["electrico", "gasolina"]:
            self.tipo = tipo
