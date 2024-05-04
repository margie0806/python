# Variables para almacenar los datos
cantidad_hombres = 0
cantidad_mujeres = 0
altura_total = 0
cantidad_altura_mayor_170 = 0
cantidad_altura_menor_150 = 0

# Bucle para solicitar los datos de los alumnos
while True:
    # Solicitar datos
    sexo = input("Ingrese el sexo del alumno (M/F): ")
    if sexo.upper() == 'M':
        cantidad_hombres += 1
    elif sexo.upper() == 'F':
        cantidad_mujeres += 1
    else:
        print("Sexo no válido. Por favor, ingrese 'M' para masculino o 'F' para femenino.")
        continue
    
    edad = int(input("Ingrese la edad del alumno (0 para finalizar): "))
    if edad == 0:
        break
    
    altura = float(input("Ingrese la altura del alumno en cm: "))
    
    # Actualizar estadísticas
    altura_total += altura
    if altura > 170:
        cantidad_altura_mayor_170 += 1
    elif altura <= 150:
        cantidad_altura_menor_150 += 1

# Calcular la altura promedio
if cantidad_hombres + cantidad_mujeres > 0:
    altura_promedio = altura_total / (cantidad_hombres + cantidad_mujeres)
else:
    altura_promedio = 0

# Mostrar resultados
print("\nResultados:")
print("Cantidad de hombres:", cantidad_hombres)
print("Cantidad de mujeres:", cantidad_mujeres)
print("Altura promedio:", altura_promedio, "cm")
print("Cantidad de alumnos con altura mayor a 170 cm:", cantidad_altura_mayor_170)
print("Cantidad de alumnos con altura menor o igual a 150 cm:", cantidad_altura_menor_150)