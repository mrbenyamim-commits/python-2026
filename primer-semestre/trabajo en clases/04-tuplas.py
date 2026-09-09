#tipo string
zapatos = ("nike", "adidas", "adobe")

print(f"{type(zapatos)}: {zapatos}")

#cestructura de datos complejos
extras = ([1,2,3,4,5], ("jose antonio", "roberto",), "soya", ("zapatos", "color"), 5)

for i in range (len(extras)):
    print(f"\n {type(extras[i])}: {extras[i]}")

plantas = ["papa", "zanahoria", "zapato"]
plantas.pop() #eliminar el ultimo elemento
print(plantas)

"""zapatos.pop()
print(zapatos)
esto daria error debido a que las tuplas son in-mutables"""

print(f"\n la primera planta es: {plantas.index("papa")}")
