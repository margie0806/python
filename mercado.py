# leer el valor de la compra 
precio = int(input("ingrese el valor de la compra (o ingrese 0 para salir):"))

if precio == 0:
    
     break # salir del bucle si se ingresa 0

balotaRoja = (precio*10)/100
balotaVerde = -(precio*15)/100
balotaAzul = (precio*20)/100
balotaAmarilla = (precio*50)100
balotaNegra = (precio*100)/100

 #calcular el descuento segun el color de la balota
if precio > 50000:   
        balota =input("¿que balota saco?").lower() #covertir a minuscula para evitar errores
if balota =="roja":
        print(f"su descuento es {balotaRoja}")
elif balota == "verde":
        print(f" su descuento es de {balotaVerde}")
elif balota == "Azul":
        print(f:su descuento es de {balotaAzul}")
elif balota == "Amarilla":
        print(f"su descuento es de {balotaAmarilla}")
elif balota == "negra":
        print(f" su descuento es de {balotaNegra}")
else:
        print("no tiene descuento, la compra no supera los 50000")