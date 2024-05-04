def main():
    # Inicializamos los contadores
    menor_a_50 = 0
    entre_50_y_70 = 0
    entre_70_y_80 = 0
    mayor_a_80 = 0
    
    # Iteramos sobre los 23 estudiantes
    for i in range(1, 24):
        # Solicitamos la calificación del estudiante
        calificacion = int(input(f"Ingrese la calificación del estudiante {i}: "))
        
        # Verificamos en qué rango de calificación cae el estudiante y actualizamos los contadores
        if calificacion < 50:
            menor_a_50 += 1
        elif calificacion < 70:
            entre_50_y_70 += 1
        elif calificacion < 80:
            entre_70_y_80 += 1
        else:
            mayor_a_80 += 1
    
    # Imprimimos los resultados
    print("Cantidad de estudiantes con calificación menor a 50:", menor_a_50)
    print("Cantidad de estudiantes con calificación entre 50 y 69:", entre_50_y_70)
    print("Cantidad de estudiantes con calificación entre 70 y 79:", entre_70_y_80)
    print("Cantidad de estudiantes con calificación de 80 o más:", mayor_a_80)

# Llamamos a la función principal para ejecutar el programa
if __name__ == "__main__":
    main()