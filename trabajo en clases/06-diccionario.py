denial = dict(
    nombre = "denial",
    edad = 18,
    ciudad = "castro",
    fecha_de_ingreso = "18-abril-2026",
    motivo_de_ingreso = "se rompio la pierna",
    informacion_extra = dict(
        sangre = "O+",
        nivel_de_daño = "alto",
        alergias = "ninguna"
    )
)

def informacion(texto, paciente):
    for i in range (len(paciente)):
        pocision = texto[i].replace(" ", "_")
        #el ".get" si no existe el terminal aparecera como "none", en caso de poner una , y luego un string salgra el string
        print(f"- {texto[i]}: {paciente.get(pocision, "(dato no encontrado)")}")

info = ["nombre", "edad", "ciudad", "fecha de ingreso", "motivo de ingreso", "informacion extra", "sexo"]

denial["sexo"] = "masculino"

print("\n ============-PACIENTE 1-============ \n")
informacion(info, denial)

print(f" key: {denial.keys()} \n \n values: {denial.values()} \n \n items: {denial.items()} ")
print(len(denial))
print(len(denial["informacion_extra"]))


denial.update({"nombre": "pablo", "edad": 21})

#elimina el valor solicitado
del(denial["sexo"])

#elimina una clave y la retorana a su ultimo valor
extras = denial.pop("informacion_extra")

print("\n ============-UPDATE PACIENTE 1-============ \n")
informacion(info, denial)

print( f"\ndatos extra eliminados: {extras}")

jesus = denial.copy()

jesus["nombre"] = "jesus"

print("\n ============-PACIENTE 2-============ \n")
informacion(info, jesus)

jesus.clear() # vacia todo el interior del diccionario "{}"

pato = {}

pato["jola"] = "no"
pato["jamon"]= ["soprole","joseluis"]
pato["jamon"].append("zanahoria")

print(pato)

