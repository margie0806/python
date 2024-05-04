# Inicializamos la variable suma
suma = 0

# Iteramos 10 veces para ingresar los números
for i in range(10):
    # Pedimos al usuario que ingrese un número negativo
    numero = int(input("Ingrese un número negativo: "))
    
    # Verificamos si el número ingresado es negativo
    if numero < 0:
        # Sumamos el número negativo a la suma total multiplicado por -1 para convertirlo a positivo
        suma += -numero
    else:
        # Si el número no es negativo, mostramos un mensaje de error y reducimos en uno el contador para que el usuario vuelva a ingresar un número negativo
        print("El número ingresado no es negativo. Intente de nuevo.")
        i -= 1

# Imprimimos la suma de los números convertidos a positivos
print("La suma de los números convertidos a positivos es:", suma)