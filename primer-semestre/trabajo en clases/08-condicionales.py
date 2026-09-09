from colorama import init, Fore

print("If y else")

licencia = True
edad = 18
auto = True

if licencia and edad >= 18:
    print(Fore.RED + "Puedes manejar")
elif auto:
    print(Fore.YELLOW +"tengo auto pero no licencia")
else:
    print(Fore.PURPLE +"no puedo conducir ni tengo auto")

licencia2 = False
edad2 = 17
auto2 = True

if licencia and edad <= 18:
    print(Fore.RED + "Puedes manejar")
elif auto:
    print(Fore.YELLOW +"tengo auto pero no licencia")
else:
    print(Fore.PURPLE +"no puedo conducir ni tengo auto")