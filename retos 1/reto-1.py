notas = []
bucle = 3
for i in range (3):
    notas.append(float(input(f"porfavor ingrese su nota n°{i+1}: ")))
    if notas[i] <= 1.0 and notas[i] >= 7.0:
        print(f"nota n°{i+1} añadida")
    else:
        print("los datos no fueron registrados, porfavor ingrese la nota de forma corecta con un unmero entre 1.0 al 7.0")
        notas.pop
        i= i-1
        bucle = bucle +1

nota_1 = notas[0]
nota_2 = notas[1]
nota_3 = notas[2]

promedio = (nota_1 * 0.4) + (nota_2 * 0.4) + (nota_3 * 0.2)

print("\n============================notas============================\n")
print(f"la primera nota fue: {notas[0]} y vale un 40% \nla segunda nota fue: {notas[1]} y vale un 40% \n y la tercera nota fue: {notas[2]} y vale un 20% \nel promedio final fue: {promedio}")
