# Programa para calcular el promedio semanal del clima
# Enfoque: Programación Orientada a Objetos (POO)

class ClimaSemanal:
    """
    Clase que representa la información climática semanal.
    """

    def __init__(self):
        # Encapsulamiento: atributo privado
        self.__temperaturas = []

    def ingresar_temperaturas(self):
        """
        Método para ingresar las temperaturas diarias.
        """
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.__temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Método que calcula y retorna el promedio semanal.
        """
        return sum(self.__temperaturas) / len(self.__temperaturas)


def main():
    """
    Función principal del programa.
    """
    print("Cálculo del promedio semanal del clima (POO)")
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")


# Ejecución del programa
main()