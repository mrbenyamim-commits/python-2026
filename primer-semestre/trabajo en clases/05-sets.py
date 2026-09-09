colores_primarios = {"azul","amarillo","rojo"}
colores_secundarios = set(["verde", "naranja", "violeta"])

print(f"\nconjunto 1: {colores_primarios}")
print(f"\nconjunto 2: {colores_secundarios}")

# crear un nuevo conjunto con duplicados
colores_extras = {"azul","verde","azul","rojo", "verde"}

print(f"\nconjunto 3: {colores_extras}") #el set tiene la propiedad de que no permite duplicados

colores_extras.add("lila")

print(f"\nconjunto 3 actualizado: {colores_extras}")

colores_extras.discard("lila")

print(f"\nconjunto 3 actualizado: {colores_extras}")

print(f"\nla diferencia entre el conjunto 1 y 3 es: {colores_primarios.difference(colores_extras)}")