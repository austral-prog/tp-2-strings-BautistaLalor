def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    nombre = input("Ingresar nombre: ")
    print(f"Contiene a: {'a' in nombre.lower()}")
    print(f"Contiene e: {'e' in nombre.lower()}")
    print(f"Contiene i: {'i' in nombre.lower()}")
    print(f"Contiene o: {'o' in nombre.lower()}")
    print(f"Contiene u: {'u' in nombre.lower()}")
