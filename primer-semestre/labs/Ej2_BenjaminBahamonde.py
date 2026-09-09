codigo_identificador = " ___icinf-2026_ula___ "

while True:
    registro = input("porfavor ingrese codigo de acceso: ")

    registro = registro.replace("_","") #remplazar los _ por espacios vacios
    codigo_identificador = codigo_identificador.replace("_","")
    
    registro = registro.upper()
    codigo_identificador = codigo_identificador.upper()

    if registro.strip() == codigo_identificador.strip():
        print(f"\nfelicidades la clave: {codigo_identificador.upper()} fue ingresado con exito")
        break
    else:
        print("\nel codigo de acceso es incorrecto pruebe otra vez \n")