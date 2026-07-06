import json

ARCHIVO_ALUMNOS = "productos.json"

def cargar_datos():
    """
    Lee los datos desde productos.json. 
    Si el archivo no existe o está vacío, lo inicializa creando una lista vacía.
    """
    with open(ARCHIVO_ALUMNOS, 'a+') as archivo:
        archivo.seek(0)
        contenido = archivo.read()

        if contenido == "":
            datos = []  
        else:
            archivo.seek(0)
            datos = json.load(archivo)

    return datos

def guardar_datos(alumnos: list) -> None:
    """
    Guarda la lista de productos en productos.json.
    Args:
        alumnos (list): La lista de productos a guardar.
    """
    with open(ARCHIVO_ALUMNOS, 'w') as archivo:
        json.dump(alumnos, archivo, indent=4)