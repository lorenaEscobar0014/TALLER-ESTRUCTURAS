"""
ENTRADAS
Nombre-->str-->nombre
Pago de la hora-->float-->pg
Horas trabajadas-->int-->ht
Horas extra-->int-->he
numero hijos-->int-->nj
SALIDAS
Asignaciones-->float-->a
Deducsiones-->float-->d
Sueldo neto-->float-->sn
"""
#if(hj>0):
#  sueldobase=sueldobase+173_000

nombre=str(input("Ingrese su nombre: "))
pg=float(input("Ingrese el valor de la hora: "))
ht=int(input("Ingrese las horas trabajadas: "))
he=int(input("Ingrese las horas extra trabajadas:"))
nj=int(input("Digite la cantidad de hijos: "))
a=(float(pg*ht))
b=(float(pg*0.25))
c=((b+pg)*he)
#sueldo base
d=(float(a+c))
e=(float(d*0.14))
f=(float(d-e))
h=(float(250000+173000+180000))
g=(float(f+250000+180000))
if(nj>0):g+173000

print(("Las asignaciones son: ")+str(h))
print(("Las deducciones son: ")+str(e))
print(("El sueldo neto del mes de diciembre es de: ")+str(g))