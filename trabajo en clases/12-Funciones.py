def multiplicion(x):
    return x * 10

y = multiplicion(5)
print(f"El resultado de la función es: {y}")

def resta(a, b):
    return a - b
resultado = resta(10, 3)
print(f"El resultado de la resta es: {resultado}")

def calcular_potencia(base, exponente):
    return base ** exponente
potencia = calcular_potencia(2, 3)
print(f"El resultado de la potencia es: {potencia}")

def factorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return n + factorial_recursivo(n-1)

print(factorial_recursivo(5))

def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1 