#crear lista vacia
aprendices = []
edades = []
# Llenar las listas solicitando datos por teclado
for _ in range(5):  # Ajusta el rango según sea necesario
    aprendiz = input("Ingrese el nombre del aprendiz: ")
    edad = int(input(f"Ingrese la edad de {aprendiz}: "))
    aprendices.append(aprendiz)
    edades.append(edad)

# Imprimir las listas
print("Aprendices:", aprendices)
print("Edades:", edades)

# Mostrar el aprendiz con la mayor edad
indice_max_edad = edades.index(max(edades))
print("Aprendiz con la mayor edad:", aprendices[indice_max_edad])

# Insertar el nombre de la instructora en la posición 1
instructora = input("Ingrese el nombre de la instructora: ")
aprendices.insert(1, instructora)

# Contar cuántos aprendices tienen 18 años
conteo_18 = edades.count(18)
print(f"{conteo_18} aprendices tienen 18 años.")

# Agregar un aprendiz 'x' al final de la lista
aprendices.append('x')

# Eliminar el nombre de la instructora de la lista
aprendices.remove(instructora)

# Buscar un dato en la lista de aprendices
dato_buscar = input("Indique un dato a buscar en la lista de aprendices: ")
if dato_buscar in aprendices:
    print(f"{dato_buscar} está en la lista.")
else:
    print(f"{dato_buscar} no está en la lista.")

# Mostrar los primeros 10 aprendices de la lista
print("Primeros 10 aprendices:", aprendices[:10])

# Mostrar los últimos 10 aprendices de la lista
print("Últimos 10 aprendices:", aprendices[-10:])

# Mostrar del elemento 10 al elemento 20
print("Elemento 10 al elemento 20:", aprendices[9:20])