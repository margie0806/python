#un grupo de 10 estudiantes presentan un examen de algoritmia.

def calcular calificaciones

malo_50 = 0
regular_50_70 = 0
bueno_70_80 = 0
exelente_80 = 0

calificacion1 = int(input("inserte la calificacion del estudiante 1"))
calificacion2 =int(input("inserte la calificacion del estudiante 2"))
calificacion3 =int(input("inserte la calificacion del estudiante 3"))
calificacion4 =int(input("inserte la calificacion del estudiante 4"))
calificacion5 =int(input("inserte la calificacion del estudiante 5"))
calificacion6 =int(input("inserte la calificacion del estudiante 6"))
calificacion7 =int(input("inserte la calificacion del estudiante 7"))
calificacion8 =int(input("inserte la calificacion del estudiante 8"))
calificacion9 =int(input("inserte la calificacion del estudiante 9"))
calificacion10 =int(input("inserte la calificacion del estudiante 10"))

#calificacion 1
if calificacion1 > 80:
    exelente_80 += 1 
elif calificacion1 > 70 and calificacion1 < 80:
    bueno_70_80 +=1
elif calificacion1 > 50 and calificacion1 < 70:
    regular_50_70 +=1
    
#calificacion 2
if calificacion2 > 80:
   exelente_80 += 1
elif calificacion2 > 70 and calificacion1 < 80:
     bueno_70_80 += 1
elif calificacion2 > 50 and calificacion1 <70:
    regular_50_70 +=1
elif calificacion2 < 50:
    malo_50 += 1
    
#califiacion 3
if calificacion3 >80:
    exelente_80 +=1
elif calificacion3 > 70 and calificacion > 80:
    bueno_70_80 +=1
elif calificacion > 50 and calificacion > 70;
     regular_50_70 += 1
elif calificacion3 < 50:
    malo_50 += 1
    
#calificacion 4
if calificacion4 > 80:
     exelente_80 += 1
elif calificacion4 > 70 and calificacion1 < 80:
     
     bueno_70_80

    







for i in range (10)
 calificacion = float(input)("ingrese la calificacion de los estudiantes") {}:".format
 while calificacion < 1 or calificacion > 100:
 print("la calificacion debe estar entre 1 y 100.")
 calificacion=float(input("ingrese la calificacion del estudiantes{}¨:
     for calificacion in calificaciones
     if calificacion<50:
         cantidad_<_50 +=1
         elif calificacion < 70:
         cantidad_50_70 +=1
     elif calificaion <80:
         cantidad_70_80 += 1
    else:
        cantidad_mayor_80 += 1

print("cantidad de estudiantes con calificacion menor a 50:",cantidad_menor_50)
print("cantidad de estudiantes con calificacion entre 50 y 69:",cantidad_50_70)
print("cantidad de estudiantes con calificacion ente 70 y 79: ", cantidad_70_80) 
print("cantidad de estudiantes con calificacionde 80 o mas:",cantidad_mayor_80)

if _ _name_ _ _== ":
main()
