import random
IA = dict(
    piedra = 0,
    papel = 0,
    tijera = 0
)

resultado = dict(
    AI = 0,
    EMPATE = 0,
    JUGADOR = 0
)

estados = ["IA", "empate", "JUGADOR"]

opciones = ["piedra", "papel", "tijera"]

def mejora(diccionario_ia, opcion):
    match opcion:
        # Si elige piedra (opción "1" o "piedra")
        case "1" | "piedra":
            diccionario_ia["piedra"] += 1
        
        # Si elige papel (opción "2" o "papel")
        case "2" | "papel":
            diccionario_ia["papel"] += 1
            
        # Si elige tijera (opción "3" o "tijera")
        case "3" | "tijera":
            diccionario_ia["tijera"] += 1

def eleccion_IA(ia, opciones, eleccion):
    match (ia["piedra"], ia["papel"], ia["tijera"]):
        # 1. Piedra es el mayor de todos
        case (p, pa, t) if p > pa and p > t:
            eleccion = opciones[1]  
        # 2. Papel es el mayor de todos
        case (p, pa, t) if pa > p and pa > t:
            eleccion = opciones[2]  
        # 3. Tijera es el mayor de todos
        case (p, pa, t) if t > p and t > pa:
            eleccion = opciones[0]  
        # 4. Todos son iguales
        case (p, pa, t) if t == p == pa:
            eleccion = random.choice(opciones)  
        # 5. Tijera y Piedra empatan (y son mayores que Papel) -> Saltamos el de en medio (Papel)
        case (p, pa, t) if t == p and t > pa:
            opciones_filtradas = opciones[:1] + opciones[2:]
            eleccion = random.choice(opciones_filtradas)
        # 6. Piedra y Papel empatan (y son mayores que Tijera) -> Eliminamos Tijera
        case (p, pa, t) if p > t and p == pa:
            opciones_filtradas = opciones[:2]  # ["piedra", "papel"]
            eleccion = random.choice(opciones_filtradas)
        # 7. Tijera y Papel empatan (y son mayores que Piedra) -> Eliminamos Piedra
        case (p, pa, t) if t > p and t == pa:
            opciones_filtradas = opciones[1:]  # ["papel", "tijera"]
            eleccion = random.choice(opciones_filtradas)
    print(f"la IA a usado {eleccion}")

def victorias(eleccion, el_IA, contador, estados):   
    match (eleccion, el_IA, contador):
        case (pj, ia, co) if pj == ia:
            print("empate")
            co["empate"] += 1
        case (pj, ia, co) if (pj == "tijera" and ia == "piedra") | (pj == "papel" and ia == "tijera") | (pj == "piedra" and ia == "papel"):
            print("la IA a gana")
            co["AI"] += 1
        case (pj, ia, co) if (ia == "tijera" and pj == "piedra") | (ia == "papel" and pj == "tijera") | (ia == "piedra" and pj == "papel"):
            print("el jugador a ganado")
            co["JUGADOR"] += 1
    



eleccion = "no"

print("hora de jugar piedra papel o tijera")

turno = 0
fin ="no"

while not(fin.upper() == "SI" or fin.upper() == "S"):
    turno += 1
    print(f"\n=====================turno:{turno}===================\n")
    opcion = input("eliga: \n1. piedra \n2. papel \n3. tijera \nelige: ")
    match opcion:
        case "1":
            opcion = "piedra"
        case "2":
            opcion = "papel"
        case "3":
            opcion = "tijera"

    if len(opcion) >= 5:
        print(f"\nel jugador uso: {opcion}")

        eleccion_IA(IA, opciones, eleccion)

        mejora(IA, opcion)

        victorias(opcion, eleccion, resultado, estados)

        fin = input("desea terminar? (si/no)\n")

    else:
        turno -= 1
        print("un dato fue ingresado incorrectamente")  