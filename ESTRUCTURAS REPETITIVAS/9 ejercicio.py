def calcular_promedio_edades(alumnos):
    # Inicializamos variables para almacenar la suma de edades de hombres, mujeres y total
    suma_edades_hombres = 0
    cantidad_hombres = 0
    suma_edades_mujeres = 0
    cantidad_mujeres = 0
    suma_edades_total = 0
    cantidad_total = 0

    for alumno in alumnos:
        edad = alumno['edad']
        genero = alumno['genero']
        # Actualizamos la suma de edades y cantidad según el género del alumno
        if genero == 'hombre':
            suma_edades_hombres += edad
            cantidad_hombres += 1
        elif genero == 'mujer':
            suma_edades_mujeres += edad
            cantidad_mujeres += 1
        
        # Actualizamos la suma de edades y cantidad para el total
        suma_edades_total += edad
        cantidad_total += 1

    # Calculamos los promedios
    promedio_edad_hombres = suma_edades_hombres / cantidad_hombres if cantidad_hombres > 0 else 0
    promedio_edad_mujeres = suma_edades_mujeres / cantidad_mujeres if cantidad_mujeres > 0 else 0
    promedio_edad_total = suma_edades_total / cantidad_total if cantidad_total > 0 else 0

    return promedio_edad_hombres, promedio_edad_mujeres, promedio_edad_total

# Ejemplo de uso
alumnos = [
    {'nombre': 'Juan', 'genero': 'hombre', 'edad': 20},
    {'nombre': 'María', 'genero': 'mujer', 'edad': 22},
    {'nombre': 'Pedro', 'genero': 'hombre', 'edad': 19},
    {'nombre': 'Ana', 'genero': 'mujer', 'edad': 21},
]

promedio_hombres, promedio_mujeres, promedio_total = calcular_promedio_edades(alumnos)

print("Promedio de edad de hombres:", promedio_hombres)
print("Promedio de edad de mujeres:", promedio_mujeres)
print("Promedio de edad total del grupo:", promedio_total)