def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    nombre_del_usuario = input("Ingresar primer nombre: ")
    apellido_del_usuario = input("Ingresar apellido: ")
    print(nombre_del_usuario.lower() + " " + apellido_del_usuario.lower())
    print(nombre_del_usuario.title() + " " + apellido_del_usuario.title())
    print(nombre_del_usuario.upper() + " " + apellido_del_usuario.upper())
    print(f"\t{nombre_del_usuario.lower()} {apellido_del_usuario.lower()}")
