censo_2017 = {
    14: {
        "nombre": "Los Ríos",
        "superficie": 18429,
        "habitantes": 404432
    },
    12: {
        "nombre": "Magallanes",
        "superficie": 1382291,
        "habitantes": 166533
    }
}
def hello_world(hola):
    print(hola)

tabla_extras = dict(
    Capital = ["Valdivia", "Punta Arena"],
    Comuna_Sugeridas =[ ["Río Bueno","La Unión", "Paillaco"], ["Cabo de Hornos", "Puerto Williams", "Porvenir"]],
    cordenadas_simuladas = ((73.4, -39.3), (-57.1, 46.9)),
    zona_exclusiva = [{"urbana", "fronteriza"}, {"urbana", "militar", "rural"}]
)
i = 14
for x in range(2):
    match censo_2017:
        case c:
            densidad = c[i]["habitantes"] / c[i]["superficie"]
            c[i].update({"densidad": densidad})
            c[i].update({"capital": tabla_extras["Capital"][x]})
            c[i].update({"comuna": tabla_extras["Comuna_Sugeridas"][x]})
            c[i].update({"cordenadas simuladas": tabla_extras["cordenadas_simuladas"][x]})
    i -= 2

censo_2017.update({"nombre": "Magallanes y Antartica Chilena"})
fin = "no"

while not(fin.upper() == "SI" or fin.upper() == "S"):
    buscar = int(input("porfavor ingrese la ID de la region que desea buscar (12 | 14) \n| "))
    match buscar:
        case b:
            hello_world(f"\nlas comunas son:")
            for c in range(len(censo_2017[b]["comuna"])):
                hello_world(f"{censo_2017[b]["comuna"][-len(censo_2017[b]["comuna"])+c]}")


    fin = input("¿desea acabar la busqueda? (si/no)\n")