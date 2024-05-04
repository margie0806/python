positivos = 0
negativos = 0
neutros = 0

for i in range(20):
    numero = int(input("Ingrese un número entero: "))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        neutros += 1

print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)
print("Cantidad de números neutros:", neutros)