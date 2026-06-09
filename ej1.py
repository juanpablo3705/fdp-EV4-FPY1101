# inicializar diccionario vacio:
diccionario = {}

# importar funciones:
import funcionesej1 as fn

# menú principal:
while True:

    print("MENU PRINCIPAL")
    print("1. Ingresar usuario")
    print("2. Buscar usuario")
    print("3. Eliminar usuario")
    print("4. Salir")

    while True:
        try:
            opcion_menu = int(input("Ingrese una opción del menú: "))
            break
        except ValueError:
            print("Error, debe ingresar sólo números, no letras.")

    match opcion_menu:
        case 1:
            fn.ingresar_usuario(diccionario)
        case 2:
            fn.buscar_usuario(diccionario)
        case 3: 
            fn.eliminar_usuario(diccionario)
        case 4:
            print("Saliendo...")
            break
        case _:
            print("Error, debe ingresar una opción del 1 al 4.")