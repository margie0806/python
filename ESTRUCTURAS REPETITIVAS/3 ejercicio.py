def calcular_promedio(calificaciones):
    total = sum(calificaciones)
    promedio = total / len(calificaciones)
    return promedio

def encontrar_maxima(calificaciones):
    maxima = max(calificaciones)
    return maxima

def encontrar_minima(calificaciones):
    minima = min(calificaciones)
    return minima
def main():

    calificaciones = [85, 90, 75, 95, 80, 88, 92, 70, 85, 78, 83, 79, 91, 87, 84, 89, 93, 77, 82, 86]

    promedio = calcular_promedio(calificaciones)
    maxima = encontrar_maxima(calificaciones)
    minima = encontrar_minima(calificaciones)

    print("El promedio de calificaciones es:", promedio)
    print("La calificación más alta es:", maxima)
    print("La calificación más baja es:", minima)

if __name__ == "__main__":
    main()