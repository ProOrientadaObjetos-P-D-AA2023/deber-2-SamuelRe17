"""

"""
# Crear dos objetos de la clase 01

# objeto 01

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"Mi nombre es {self.nombre} y tengo {self.edad} años."


persona1 = Persona("Juan", 30)

print(persona1)


# objeto 02

class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
    
    def __str__(self):
        return f"Mi nombre es {self.nombre}, tengo {self.edad} años y estudio {self.carrera}."


nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
carrera = input("Ingrese la carrera del estudiante: ")


estudiante1 = Estudiante(nombre, edad, carrera)


print(estudiante1)


