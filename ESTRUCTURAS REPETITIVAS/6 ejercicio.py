def calcular_genero_personas():
    total_personas = int(input("Ingrese el total de personas en el salón de clases: "))
    
    hombres = 0
    mujeres = 0
    
    for i in range(total_personas):
        genero = input("Ingrese el género de la persona {}: (H/M) ".format(i+1)).upper()
        if genero == 'H':
            hombres += 1
        elif genero == 'M':
            mujeres += 1
        else:
            print("Género no válido. Por favor ingrese 'H' para hombre o 'M' para mujer.")

    return hombres, mujeres

cantidad_hombres, cantidad_mujeres = calcular_genero_personas()

print("Cantidad de hombres:", cantidad_hombres)
print("Cantidad de mujeres:", cantidad_mujeres)