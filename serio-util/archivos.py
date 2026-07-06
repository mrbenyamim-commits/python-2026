# Creamos un archivo llamado 'mis_notas.txt' en modo escritura ('w')
with open("mis_notas.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Nota 1: Aprender a manejar archivos.\n")
    archivo.write("Nota 2: Practicar con Python hoy por la tarde.\n")
    archivo.write("Nota 3: Estudiar estructuras de datos.\n")

print("¡Archivo creado con éxito!")

print(archivo)