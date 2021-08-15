s=float(input("Ingrese el valor de su sueldo base: "))
pv=float(input("Ingrese el valor de la primera venta: "))
sv=float(input("Ingrese el valor de la segunda venta: "))
tv=float(input("Ingrese el valor de la segunda venta: "))
a=(pv*0.10)
b=(sv*0.10)
c=(tv*0.10)
d=(a+b+c)+s
print(("El total del sueldo es de: ")+str(d))