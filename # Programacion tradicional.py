# Programa para calcular el promedio semanal del clima
# Enfoque: Programación Tradicional

def ingresar_temperaturas():
    """
    Función para ingresar las temperaturas diarias de la semana.
    Retorna una lista con las temperaturas.
    """
    temperaturas = []
    for dia in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas


def calcular_promedio(temperaturas):
    """
    Función que calcula el promedio semanal
    a partir de una lista de temperaturas.
    """
    return sum(temperaturas) / len(temperaturas)


def main():
    """
    Función principal que organiza la ejecución del programa.
    """
    print("Cálculo del promedio semanal del clima (Programación Tradicional)")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")


# Ejecución del programa
main()
