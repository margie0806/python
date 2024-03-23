# Función para contar las calificaciones en diferentes rangos
def contar_calificaciones(calificaciones):
    menor_50 = 0
    entre_50_70 = 0
    entre_70_80 = 0
    mayor_80 = 0
    
    for calificacion in calificaciones:
        if calificacion < 50:
            menor_50 += 1
        elif 50 <= calificacion < 70:
            entre_50_70 += 1
        elif 70 <= calificacion < 80:
            entre_70_80 += 1
        else:
            mayor_80 += 1
    
    return menor_50, entre_50_70, entre_70_80, mayor_80

# Lista para almacenar las calificaciones
calificaciones = []

# Solicitar las calificaciones de los 10 estudiantes
for i in range(10):
    calificacion = int(input(f"Ingrese la calificación del estudiante {i+1}: "))
    # Verificar que la calificación esté en el rango válido
    while calificacion < 1 or calificacion > 100:
        print("La calificación debe estar entre 1 y 100.")
        calificacion = int(input(f"Ingrese la calificación del estudiante {i+1}: "))
    calificaciones.append(calificacion)

# Llamar a la función para contar las calificaciones
menor_50, entre_50_70, entre_70_80, mayor_80 = contar_calificaciones(calificaciones)

# Imprimir los resultados
print("Cantidad de estudiantes con calificación menor a 50:", menor_50)
print("Cantidad de estudiantes con calificación entre 50 y 69:", entre_50_70)
print("Cantidad de estudiantes con calificación entre 70 y 79:", entre_70_80)
print("Cantidad de estudiantes con calificación de 80 o más:", mayor_80)