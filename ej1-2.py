# inicializar diccionario vacío: 
diccionario = {}

# funcion 1 ingresar usuario:
def ingresar_usuario(diccionario):

    while True:
        nombre = input("Ingrese nombre de usuario: ")
        if nombre in diccionario:
            print("Error, el nombre de usuario ya existe.")
        else:
            print("Nombre ingresado con éxito.")
            break

    while True:
        sexo = input("Ingrese el sexo del usuario (F/M): ").upper()
        if (sexo == "F") or (sexo == "M"):
            print("Sexo ingresado con éxito.")
            break
        else:
            print("Error, debe ingresar solo F o M.")

    while True:
        contrasena = input("Ingrese nueva contraseña del usuario: ")
        tiene_letra = False
        tiene_numero = False
        for caracter in contrasena:
            if caracter.isalpha():
                tiene_letra = True
            if caracter.isdigit():
                tiene_numero = True
        if (len(contrasena) >= 8) and (" " not in contrasena) and tiene_letra and tiene_numero:
            print("Nueva contraseña ingresada con éxito.")
            break
        else:
            print("Contraseña no válida. Intente otra.")

    diccionario[nombre] = [sexo, contrasena]

# funcion 2 buscar usuario:
def buscar_usuario(diccionario):

    if len(diccionario) == 0:
        print("Error. No hay usuarios registrados. Vuelva a la opción 1.")
        return
    
    nombre = input("Ingrese el nombre del usuario a buscar: ")

    if nombre in diccionario:
        sexo = diccionario[nombre][0]
        contrasena = diccionario[nombre][1]
        print(f"Usuario encontrado. Nombre: {nombre}. Sexo: {sexo}. Contraseña: {contrasena}.")
    else:
        print("Usuario no encontrado.")

# funcion 3 eliminar usuario:
def eliminar_usuario(diccionario):

    if len(diccionario) == 0:
        print("Error. No hay usuarios registrados. Vuelva a la opción 1.")
        return

    nombre = input("Ingrese nombre del usuario a eliminar: ")

    if nombre in diccionario:
        del diccionario[nombre]
        print(f"Usuario {nombre} eliminado con éxito.")
    else:
        print("Error. Usuario no encontrado.")

# menú principal:
while True:

    print("1.- Ingresar usuario")
    print("2.- Buscar usuario")
    print("3.- Eliminar usuario")
    print("4.- Salir")

    while True:
        try:
            opcion_menu = int(input("Ingrese una opción del menú: "))
            break
        except ValueError:
            print("Error, debe ingresar sólo números del 1 al 4, no letras.")

    match opcion_menu:
        case 1:
            ingresar_usuario(diccionario)
        case 2:
            buscar_usuario(diccionario)
        case 3:
            eliminar_usuario(diccionario)
        case 4:
            print("Saliendo...")
            break
        case _:
            print("Error, debe ingresar una opción del 1 al 4.")