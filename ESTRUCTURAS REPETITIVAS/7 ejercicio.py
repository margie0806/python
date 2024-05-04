def determinar_color_calcomania(placa):
    ultimo_digito = int(placa[-1])
    if ultimo_digito == 1 or ultimo_digito == 2:
        return "Amarilla"
    elif ultimo_digito == 3 or ultimo_digito == 4:
        return "Rosa"
    elif ultimo_digito == 5 or ultimo_digito == 6:
        return "Roja"
    elif ultimo_digito == 7 or ultimo_digito == 8:
        return "Verde"
    elif ultimo_digito == 9 or ultimo_digito == 0:
        return "Azul"
    else:
        return "Color no válido"

def contar_colores_calcomania(n):
    colores = {"Amarilla": 0, "Rosa": 0, "Roja": 0, "Verde": 0, "Azul": 0}
    
    for i in range(n):
        placa = input("Ingrese el último dígito de la placa del auto {}: ".format(i+1))
        color = determinar_color_calcomania(placa)
        if color != "Color no válido":
            colores[color] += 1
        else:
            print("El último dígito de la placa ingresado no es válido.")

    return colores

total_autos = int(input("Ingrese el número total de autos que entran a la ciudad de Ibagué: "))
colores_calcomania = contar_colores_calcomania(total_autos)

print("\nResultados:")
for color, cantidad in colores_calcomania.items():
    print("Calcomanías de color {}: {}".format(color, cantidad))