def tabla_de_multiplicar(numero):
    print("Tabla de multiplicar del", numero)
    print("---------------------------")
    for multiplicador in range(1, 11):
        producto = numero * multiplicador
        print(numero, "x", multiplicador, "=", producto)

def main():
    # Solicitar al usuario que ingrese un número
    numero = int(input("Ingresa un número para calcular su tabla de multiplicar: "))

    # Llamar a la función tabla_de_multiplicar con el número ingresado
    tabla_de_multiplicar(numero)

if __name__ == "__main__":
    main()