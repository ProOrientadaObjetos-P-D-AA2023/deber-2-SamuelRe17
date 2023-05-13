"""

"""

# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Mi nombre es {self.nombre} y tengo {self.edad} años.")

    def cumplir_anios(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños! Ahora tengo {self.edad} años.")

persona1 = Persona("Juan", 30)

persona1.presentarse()

persona1.cumplir_anios()



# clase 02
class Coche:
    def __init__(self, marca, modelo, anio, color):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.velocidad = 0

    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"{self.marca} {self.modelo} acelera {incremento} km/h. Velocidad actual: {self.velocidad} km/h")

    def frenar(self, decremento):
        self.velocidad -= decremento
        if self.velocidad < 0:
            self.velocidad = 0
        print(f"{self.marca} {self.modelo} frena {decremento} km/h. Velocidad actual: {self.velocidad} km/h")


mi_coche = Coche("Toyota", "Corolla", 2021, "Rojo")


mi_coche.acelerar(50)
mi_coche.frenar(20)
