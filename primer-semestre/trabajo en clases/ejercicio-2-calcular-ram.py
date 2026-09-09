ram_usada = []
tiempo = ["la mañana","el medio dia", "la tarde", "la noche"]
momento = 0

while True:
    print()
    ram_usada.append(float(input(f"porfavor ingresar la cantidad de gigas ram usadas en {tiempo[momento]}: ")))
    if ram_usada[momento] <= 0:
        print("el dato que se ingreso esta mal, porfavor ingrese el dato nuevamente")
        ram_usada.pop()
    elif momento == len(tiempo):
        print()
        break
    else:
        momento = momento + 1
    
manana = ram_usada[0]
medio_dia = ram_usada[1]
tarde = ram_usada[2]
noche = ram_usada[3]

print(f"el consumo promedio del dia es de: {sum(ram_usada)/len(ram_usada):.1} gigas ram")
print(f"el 'Rango de Operación del dias es de: {max(ram_usada) - min(ram_usada):.1}")