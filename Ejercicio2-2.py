from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"

class Planeta:
    def __init__(self, nombre=None, cantidad_satelites=0, masa=0.0,
                 volumen=0.0, diametro=0, distancia_sol=0,
                 tipo=TipoPlaneta.TERRESTRE, es_observable=False):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol  # en millones de km
        self.tipo = tipo
        self.es_observable = es_observable

    def imprimir(self):
        print(f"Nombre del planeta: {self.nombre}")
        print(f"Cantidad de satélites: {self.cantidad_satelites}")
        print(f"Masa del planeta (kg): {self.masa}")
        print(f"Volumen del planeta (km³): {self.volumen}")
        print(f"Diámetro (km): {self.diametro}")
        print(f"Distancia al Sol (millones de km): {self.distancia_sol}")
        print(f"Tipo de planeta: {self.tipo.value}")
        print(f"Es observable a simple vista: {self.es_observable}")
        print("-" * 40)

    def calcular_densidad(self):
        if self.volumen == 0:
            return 0
        return self.masa / self.volumen

    def es_planeta_exterior(self):
        UA = 149_597_870  # Unidad Astronómica en km
        distancia_km = self.distancia_sol * 1_000_000
        limite = UA * 3.4
        return distancia_km > limite

def main():
    tierra = Planeta("Tierra", 1, 5.9736e24, 1.08321e12, 12742, 150, TipoPlaneta.TERRESTRE, True)
    jupiter = Planeta("Júpiter", 79, 1.898e27, 1.43128e15, 139820, 750, TipoPlaneta.GASEOSO, True)

    for planeta in [tierra, jupiter]:
        planeta.imprimir()
        print("Densidad del planeta:", planeta.calcular_densidad())
        print("¿Es planeta exterior?", planeta.es_planeta_exterior())
        print()

if __name__ == "__main__":
    main()
