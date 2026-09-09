import hello
mis_nota = []

for i in range(5):
    nota = float(input(f"porfavor ingrese su nota n°{i+1} \n|  "))
    mis_nota.append(nota)
promedio = 0
for i in range(len(mis_nota)):
    promedio = promedio + mis_nota[i]
    hello.world(f"nota {i+1}: {mis_nota[i]}\n")
hello.world(f"\nNota Maxima: {max(mis_nota)} \nNota Minima: {min(mis_nota)} \nPromedio notas: {promedio/ len(mis_nota)}")