"""

"""
# Crear dos objetos de la clase 02

# objeto 01
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio ** 2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
    
    def __str__(self):
        return f"El círculo tiene un radio de {self.radio}, un área de {self.calcular_area():.2f} y un perímetro de {self.calcular_perimetro():.2f}."

radio = float(input("Ingrese el radio del círculo: "))


circulo1 = Circulo(radio)


print(circulo1)


# objeto 02
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
    def __str__(self):
        return f"El rectángulo tiene una base de {self.base}, una altura de {self.altura}, un área de {self.calcular_area()} y un perímetro de {self.calcular_perimetro()}."


base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))


rectangulo1 = Rectangulo(base, altura)


print(rectangulo1)


