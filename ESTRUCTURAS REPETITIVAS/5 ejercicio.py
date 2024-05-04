def calcular_promedio(pesos):
    if len(pesos) == 0:
        return 0
    total = sum(pesos)
    promedio = total / len(pesos)
    return promedio

def main():
    # Inicializar listas para almacenar los pesos de cada categoría de edad
    pesos_ninos = []
    pesos_jovenes = []
    pesos_adultos = []
    pesos_ancianos = []
# Solicitar al usuario que ingrese el peso de cada persona y su categoría de edad
    for i in range(50):
        peso = float(input("Ingresa el peso de la persona {}: ".format(i + 1)))
        categoria = input("Ingresa la categoría de edad de la persona (niño, joven, adulto, anciano): ")
        
        # Agregar el peso a la lista correspondiente según la categoría de edad
        if categoria == "niño":
            pesos_ninos.append(peso)
        elif categoria == "joven":
            pesos_jovenes.append(peso)
        elif categoria == "adulto":
            pesos_adultos.append(peso)
        elif categoria == "anciano":
            pesos_ancianos.append(peso)
        else:
            print("Categoría de edad no válida. Por favor, ingresa niño, joven, adulto o anciano.")

    # Calcular el promedio de peso para cada categoría de edad
    promedio_ninos = calcular_promedio(pesos_ninos)
    promedio_jovenes = calcular_promedio(pesos_jovenes)
    promedio_adultos = calcular_promedio(pesos_adultos)
    promedio_ancianos = calcular_promedio(pesos_ancianos)

    # Imprimir los resultados
    print("Promedio de peso de niños:", promedio_ninos)
    print("Promedio de peso de jóvenes:", promedio_jovenes)
    print("Promedio de peso de adultos:", promedio_adultos)
    print("Promedio de peso de ancianos:", promedio_ancianos)

if __name__ == "__main__":
    main()