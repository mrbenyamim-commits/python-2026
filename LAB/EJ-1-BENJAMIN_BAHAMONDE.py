


productos = [ "Pan", "Leche", "Pan", "Queso", "Leche", "Jugo", "Pan" ]

print(f"\nhay un total de {len(productos)} productos, incluyendo repetidos")

productos_sin_repetir = list(set(productos))
print(f"sin repetir hay un total de {len(productos_sin_repetir)} productos \n")


print("productos vendidos:")
for i in range(len(productos_sin_repetir)):
    s = productos_sin_repetir[i]
    print(f"producto {i+1}: {productos_sin_repetir[i]}")
    if s == "Jugo":
        p = s



match p:
    case p if p == "Jugo":
        print("el jugo ya fue vendido")
    case p if p != "Jugo":
        print("el jugo aun no fue vendido")

