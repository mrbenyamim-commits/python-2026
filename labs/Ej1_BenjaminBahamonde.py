registro_lluvia = []
registros_total = 0

for i in range (5):
    registro_lluvia.append(float(input(f"\ningrese la {i+1}°a precipitacion de 5: ")))
    registros_total = registros_total + registro_lluvia[i]

for i in range (len(registro_lluvia)):
    print(f"\nla interpretacion n°{1+i} se registro: {registro_lluvia[i]} mm de diferencia con lo esperado")

print(f"el promedio de los 5 registros es: {registros_total/len(registro_lluvia)} mm de diferencia \nel minimo registro es: {min(registro_lluvia)} mm de diferencia \nel maximo registrado es: {max(registro_lluvia)} mm de diferencia\nla brecha pluvial: {max(registro_lluvia) - min(registro_lluvia)}")