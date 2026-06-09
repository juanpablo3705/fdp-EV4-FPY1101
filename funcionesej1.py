# funcion 1 ingresar usuario:
def ingresar_usuario(diccionario):

    nombre = input("Ingrese nombre de usuario: ")
    if nombre in diccionario:
        print("Error, usuario ya existe.")
        return
    
    sexo_usuario = input("Ingrese sexo del usuario F/M: ").upper()
    if (sexo_usuario == "F") or (sexo_usuario == "M"):
        sexo_usuario = sexo_usuario
    else:
        print("Error, debe ingresar sólo F o M.")
        return
    
    contrasena_usuario = input("Ingrese la contraseña del usuario: ")

    tiene_letra = False
    tiene_numero = False

    for caracter in contrasena_usuario:
        if caracter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            tiene_letra = True

        if caracter in "0123456789":
            tiene_numero = True

    if len(contrasena_usuario) < 8:
        print("Error, la contraseña debe tener al menos 8 caracteres.")
        return

    if " " in contrasena_usuario:
        print("Error, la contraseña no puede tener espacios.")
        return

    if not tiene_letra:
        print("Error, la contraseña debe contener al menos una letra.")
        return

    if not tiene_numero:
        print("Error, la contraseña debe contener al menos un número.")
        return

    diccionario[nombre] = [sexo_usuario, contrasena_usuario]

# funcion 2 buscar usuario:
def buscar_usuario(diccionario):
    nombre = input("Ingrese nombre a buscar: ")
    if nombre in diccionario:
        sexo = diccionario[nombre][0]
        contrasena = diccionario[nombre][1]
        print(f"Nombre: {nombre}.")
        print(f"Sexo: {sexo}.")
        print(f"Contraseña: {contrasena}.")
    else:
        print("El usuario NO existe.")

# funcion 3 eliminar usuario:
def eliminar_usuario(diccionario):
    nombre = input("Ingrese nombre de usuario a eliminar: ")
    if nombre in diccionario:
        del diccionario[nombre]
        print("¡Usuario eliminado!")
    else:
        print("No se pudo eliminar usuario!")