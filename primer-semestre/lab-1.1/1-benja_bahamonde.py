import hello
nombre = input("\nporfavor ingrese su nombre completo ")
edad = int(input("\nporfavor ingrese su edad (como numero) "))
carrera= input("\nporfavor ingrese su carrera ")
estatura = float(input("\nporfavor ingrese su edad en metros (poniendo decimales) "))

preguntas = ["Nombre", "Edad", "Carrera", "Estatura"]
datos= {
    "Nombre": nombre,
    "Edad": edad,
    "Carrera": carrera,
    "Estatura": estatura
}

extras= ["", "años", "", "metros"]

for i in range (len(datos)):
    d = preguntas[i]
    hello.world(f"\n {preguntas[i]}: {datos[d]} {extras[i]}")