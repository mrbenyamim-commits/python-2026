class objeto():
    def __init__(self, nombre, tipo, dano, effectos):
        self.nombre = nombre
        self.tipo = tipo
        self.dano = dano
        self.effectos = effectos
objetos = []


palabras = ["dime el nombre del objeto:  ", "cual es su efecto? \n 1- curar \n 2- daña \n 3- defiende \n", "del 1 al 10 ¿cual es su potencia? ", "cual es su effecto? "]
for i in range(len(palabras)):
    objetos.append(input(f"\n {palabras[i]}"))

ob = objeto(objetos)

print(ob)

