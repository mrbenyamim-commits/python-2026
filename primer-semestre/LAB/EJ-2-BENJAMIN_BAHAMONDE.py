notas = {
"Ana": 6.2,
"Luis": 4.8,
"Pedro": 3.9,
"Sofía": 5.5
}

alumnos = ["Ana", "Luis", "Pedro", "Sofía"]

for i in range (len(notas)):
    estudiante = alumnos[i]
    nota = notas[estudiante]
    match (nota, estudiante):
        case (n, e) if n >= 4.0:
            print(f"{e} a aprobado con: {n}")
        case (n, e) if n < 4.0:
            print(f"{e} a desaprobado con: {n}")
            