temperatura = [12.5, 14.2, 11.8]

print(f"El lunes tuvo {temperatura[0]}°C,  el martes tuvo {temperatura[1]}°C y el miercoles tenia {temperatura[2]}°C")

promedio = round(sum(temperatura) / 3)

print(f"En promedio la semana tuvo {promedio}°C.")
print(f"El dia con mas calor fue: {max(temperatura)}°C y el dia mas frio fue: {min(temperatura)}°C.")
print(f"con una diferencia de: {round(max(temperatura) - min(temperatura))}°C. ")

