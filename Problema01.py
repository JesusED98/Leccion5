tornillo = 5
tuerca = 3
arandela = 1
tor = int (input ("Introduce número de tornillos: "))
tuer = int (input ("Introduce número de tuercas: "))
ar = int (input ("Introduce número de arandeles: "))
suma = tor * tornillo + tuer * tuerca + ar * arandela
if tor > tuer:
    print("Verifica el pedido")
    print("Costo Total: ",suma)
else:
    print("Costo Total: ",suma)