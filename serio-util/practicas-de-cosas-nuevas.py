# Ejemplo de uso de la sentencia 'match' (disponible en Python 3.10+)
# El match funciona como un switch-case avanzado para comparar patrones


def evaluar_comando(comando):
    match comando.split():
        case ["ayuda"]:
            print("Lista de comandos: ayuda, salir, mover <direccion>")
        case ["salir"]:
            print("Cerrando el programa...")
            return False
        case ["mover", "norte" | "sur" | "este" | "oeste"] as movimiento:
            print(f"Personaje se desplaza hacia el {movimiento[1]}")
        case ["mover", direccion]:
            print(f"La dirección '{direccion}' no es válida.")
        case _:
            print("Comando no reconocido.")
    return True

# Prueba del match
print("--- Sistema de Comandos ---")
evaluar_comando("ayuda")
evaluar_comando("mover norte")
evaluar_comando("mover arriba")
evaluar_comando("desconocido")