lista1 = ["Germán", 18, True, "Germán", "Germán", "Germán"]
ramos = []
n = list([1,2,3,4,5])
print(lista1[0])

print(lista1.count("Germán"))
print(ramos)

ramos.append("Química")
print(ramos)
ramos.append("Habilidades Comunicativas")
print(ramos)
ramos.append("Programacion")
print(ramos)
ramos.insert(0, "Introducción a la Matemática")
print(ramos)
ramos[2] = "Habilidades Comunicativas para ingenieros/as"
print(ramos)

ramos.pop()
print(ramos)

ramos.sort()
print(ramos)

n.sort()
print(n)

ramos.sort(key=len)
print(ramos)

ramos_segundo_semestre = ["Ciudadanía", "Algebra","Introducción a la Física"]
print(ramos_segundo_semestre)

ramos.extend(ramos_segundo_semestre)
print(ramos)

ramos_largo = list(filter(lambda x: len(x) > 7 , ramos_segundo_semestre))
print(ramos_largo)