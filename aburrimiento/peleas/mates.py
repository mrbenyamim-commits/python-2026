import math as mt
def segmento():
    a = (0 , 2)
    b = (-3 , -1)
    c = (-4 , 3)

    line = input("seleccione el primer termino ")
    linea = input("seleccione el segundo termino ")

    match (line, linea):
        case (l1,l2) if l1 == "a" and l2 == "b":
            l1 = a 
            l2 = b
            print("\n", mt.sqrt((l2[0] - l1[0])**2 + (l2[1] - l1[1])**2 ))

        case (l1,l2) if l1 == "b" and l2 == "c":
            l1 = b
            l2 = c
            print("\n", mt.sqrt((l2[0] - l1[0])**2 + (l2[1] - l1[1])**2 ))

        case (l1,l2) if l1 == "c" and l2 == "a":
            l1 = c
            l2 = a
            print("\n", mt.sqrt((l2[0] - l1[0])**2 + (l2[1] - l1[1])**2))

def igualdad(x):
    y = 1 - (x)**2
    print("valor de y:", y)

x = int(input("valor de x: "))

igualdad(x)

 