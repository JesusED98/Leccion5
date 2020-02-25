t = int (input ("Capacidad del tanque: "))
print("Porcentaje del medidor de gas")
print("  Completo     - 100%")
print("  Tres cuartos -  75%")
print("  La mitad     -  50%")
print("  Un cuarto    -  25%")
m = int (input ("Lectura del medidor: "))
mi = int (input ("Millas por galon: "))
g = t * (m/100) * mi
if g > 200:
    print("¡Seguro, proceder!")
else:
    print("¡Consigue gasolina!")