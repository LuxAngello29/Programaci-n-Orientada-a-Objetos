from enum import Enum

class TipoCombustible(Enum):
    GASOLINA = "Gasolina"
    BIOETANOL = "Bioetanol"
    DIESEL = "Diésel"
    BIODIESEL = "Biodiésel"
    GAS_NATURAL = "Gas Natural"

class TipoAutomovil(Enum):
    CIUDAD = "Carro de ciudad"
    SUBCOMPACTO = "Subcompacto"
    COMPACTO = "Compacto"
    FAMILIAR = "Familiar"
    EJECUTIVO = "Ejecutivo"
    SUV = "SUV"

class Color(Enum):
    BLANCO = "Blanco"
    NEGRO = "Negro"
    ROJO = "Rojo"
    NARANJA = "Naranja"
    AMARILLO = "Amarillo"
    VERDE = "Verde"
    AZUL = "Azul"
    VIOLETA = "Violeta"

class Automovil:
    def __init__(self, marca, modelo, motor, tipo_combustible, tipo_automovil,
                 num_puertas, asientos, velocidad_max, color):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.num_puertas = num_puertas
        self.asientos = asientos
        self.velocidad_max = velocidad_max
        self.color = color
        self.vel_actual = 0

    def acelerar(self, incremento):
        if self.vel_actual + incremento <= self.velocidad_max:
            self.vel_actual += incremento
        else:
            print("No se puede incrementar más allá de la velocidad máxima.")

    def frenar(self, decremento):
        if self.vel_actual - decremento >= 0:
            self.vel_actual -= decremento
        else:
            self.vel_actual = 0

    def calcular_tiempo_llegada(self, distancia):
        if self.vel_actual > 0:
            return distancia / self.vel_actual
        else:
            print("El automóvil está detenido.")
            return None

    def mostrar_detalles(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Motor: {self.motor} L")
        print(f"Tipo de combustible: {self.tipo_combustible.value}")
        print(f"Tipo de automóvil: {self.tipo_automovil.value}")
        print(f"Número de puertas: {self.num_puertas}")
        print(f"Asientos: {self.asientos}")
        print(f"Velocidad máxima: {self.velocidad_max} km/h")
        print(f"Color: {self.color.value}")
        print(f"Velocidad actual: {self.vel_actual} km/h")

def main():
    auto1 = Automovil("Ford", 2018, 3.5, TipoCombustible.DIESEL, TipoAutomovil.EJECUTIVO,
                      5, 6, 250, Color.NEGRO)
    auto1.mostrar_detalles()

    auto1.vel_actual = 100
    print(f"\nVelocidad actual: {auto1.vel_actual} km/h")
    auto1.acelerar(20)
    print(f"Velocidad después de acelerar: {auto1.vel_actual} km/h")
    auto1.frenar(50)
    print(f"Velocidad después de frenar: {auto1.vel_actual} km/h")
    auto1.frenar(100)
    print(f"Velocidad después de frenar otra vez: {auto1.vel_actual} km/h")

    tiempo = auto1.calcular_tiempo_llegada(100)
    if tiempo:
        print(f"Tiempo para recorrer 100 km: {tiempo:.2f} horas")

if __name__ == "__main__":
    main()
