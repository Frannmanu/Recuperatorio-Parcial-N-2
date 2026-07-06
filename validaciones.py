def validar_codigo_unico(codigo: str, inventario: list) -> bool:
    """Valida que el código ingresado sea único en el inventario.
    
    Args:
        codigo (str): El código a validar.
        inventario (list): La lista de productos.
    Returns: 
        bool: True si el código es único, False si no lo es."""
    for i in range(len(inventario)):
        producto = inventario[i]
        if producto["codigo"] == codigo:
            return False
    return True

def pedir_cadena_no_vacia(mensaje: str) -> str:
    """Solicita al usuario una cadena de texto que no esté vacía.
    
    Args:
        mensaje (str): El mensaje a mostrar al usuario.
    Returns:
        str: La cadena ingresada por el usuario.
    """
    valor = input(mensaje)
    while valor == "":
        print("Error: El campo no puede estar vacío.")
        valor = input(mensaje)
    return valor

def pedir_numero_positivo(mensaje: str, incluir_cero: bool = False) -> float:
    """Solicita al usuario un número positivo.
    
    Args:
        mensaje (str): El mensaje a mostrar al usuario.
        incluir_cero (bool): Indica si se permite el valor cero como válido.
    Returns:
        float: El número ingresado por el usuario.
    """
    valor = float(input(mensaje))
    if incluir_cero == True:
        while valor < 0:
            print("Error: El número no puede ser negativo.")
            valor = float(input(mensaje))
    else:
        while valor <= 0:
            print("Error: El número debe ser mayor a cero.")
            valor = float(input(mensaje))
    return valor