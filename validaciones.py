def validar_codigo_unico(codigo, inventario):
    for i in range(len(inventario)):
        producto = inventario[i]
        if producto["codigo"] == codigo:
            return False
    return True

def pedir_cadena_no_vacia(mensaje):
    valor = input(mensaje)
    while valor == "":
        print("Error: El campo no puede estar vacío.")
        valor = input(mensaje)
    return valor

def pedir_numero_positivo(mensaje, incluir_cero=False):
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