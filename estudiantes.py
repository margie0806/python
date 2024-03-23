#un grupo de estudiantes presentan un examen de algoritmia.
def contar_calificaciones(calificaciones):
    # Inicializamos contadores
    menor_50 = 0
    entre_50_70 = 0
    entre_70_80 = 0
    mayor_80 = 0
    
    # Recorremos las calificaciones
    for calificacion in calificaciones:
        if calificacion < 50:
            menor_50 += 1
        elif calificacion >= 50 and calificacion < 70:
            entre_50_70 += 1
        elif calificacion >= 70 and calificacion < 80:
            entre_70_80 += 1
        else:
            mayor_80 += 1
    
    # Imprimimos los resultados
    print("Cantidad de estudiantes con calificación menor a 50:", menor_50)
    print("Cantidad de estudiantes con calificación entre 50 y 69:", entre_50_70)
    print("Cantidad de estudiantes con calificación entre 70 y 79:", entre_70_80)
    print("Cantidad de estudiantes con calificación de 80 o más:", mayor_80)

# Solicitamos las calificaciones de los estudiantes
num_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
calificaciones = []

for i in range(num_estudiantes):
    calificacion = int(input(f"Ingrese la calificación del estudiante {i+1}: "))
    while calificacion < 1 or calificacion > 100:
        print("La calificación debe estar entre 1 y 100.")
        calificacion = int(input(f"Ingrese la calificación del estudiante {i+1}: "))
    calificaciones.append(calificacion)

# Llamamos a la función para contar las calificaciones
contar_calificaciones(calificaciones)