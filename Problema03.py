a1 = float (input ("Precio por libra paquete A: "))
a2 = float (input ("Porcentaje magro del paquete A: "))
b1 = float (input ("Precio por libra paquete B: "))
b2 = float (input ("Porcentaje magro del paquete B: "))
CLA = a1/a2
CLB = b1/b2
print("Costo por libra de carne magra Paquete A: ",CLA)
print("Costo por libra de carne magra Paquete B: ",CLB)
if CLA > CLB:
    print("El paquete B es el mejor valor")
else:
    print("El paquete A es el mejor valor")