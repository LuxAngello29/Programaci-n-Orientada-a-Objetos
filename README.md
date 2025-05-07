# Programacion-Orientada-a-Objetos
class Persona:
    def __init__(self, nombre, apellido, numero_documento, anio_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_documento = numero_documento
        self.anio_nacimiento = anio_nacimiento

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Número de Documento: {self.numero_documento}")
        print(f"Año de Nacimiento: {self.anio_nacimiento}")
        print("-" * 30)

def main():
    persona1 = Persona("Ana", "Gómez", "12345678", 1995)
    persona2 = Persona("Luis", "Martínez", "87654321", 1988)

    print("Datos de la Persona 1:")
    persona1.imprimir()

    print("Datos de la Persona 2:")
    persona2.imprimir()

# Llamada a main (solo si ejecutamos el script directamente)
if __name__ == "__main__":
    main()
