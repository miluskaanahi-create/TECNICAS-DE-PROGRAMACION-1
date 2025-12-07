# ================================
# ABSTRACCIÓN
# ================================
from abc import ABC, abstractmethod

class Vehiculo(ABC):  # Clase abstracta
    @abstractmethod
    def moverse(self):
        pass


# ================================
# ENCAPSULACIÓN
# ================================
class Motor:
    def __init__(self, potencia):
        self.__potencia = potencia  # atributo privado

    def get_potencia(self):
        return self.__potencia

    def set_potencia(self, potencia):
        self.__potencia = potencia


# ================================
# HERENCIA
# ================================
class Auto(Vehiculo):  
    def __init__(self, marca, potencia):
        self.marca = marca
        self.motor = Motor(potencia)

    def moverse(self):
        return f"El auto {self.marca} se mueve por la carretera."

class Moto(Vehiculo):  
    def __init__(self, marca):
        self.marca = marca

    def moverse(self):
        return f"La moto {self.marca} se mueve rápidamente."


# ================================
# POLIMORFISMO
# ================================
def mostrar_movimiento(vehiculo):
    print(vehiculo.moverse())


# ================================
# PROGRAMA PRINCIPAL
# ================================
auto1 = Auto("Toyota", 150)
moto1 = Moto("Yamaha")

mostrar_movimiento(auto1)  
mostrar_movimiento(moto1)

print("Potencia del auto:", auto1.motor.get_potencia())
auto1.motor.set_potencia(180)
print("Nueva potencia del auto:", auto1.motor.get_potencia())
