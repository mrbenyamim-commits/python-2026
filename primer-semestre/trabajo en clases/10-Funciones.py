def mult(x):
    return x * 10

y = mult(5)
print(y)

def saludo(nombre):
    print(f"Hi my name is {nombre}")

saludo("Pipe")

def suma(a, b):
    return a + b

resultado = suma(2, 3)
print(resultado)

def resta(a, b=5):
    return a - b

resultado1 = resta(2) # sin la segunda variable
print(resultado1)

resultado2 = resta(4,4)
print(resultado2)


def potencia(base, exponente):
    return base ** exponente

resultado3 = potencia(exponente=3, base= 2)
print(resultado3)

def factorial(n):
    x = 1
    i = 2
    while i <= n:
        x += i
        i += 1
    return x
print(factorial(5))