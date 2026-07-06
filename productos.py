import validaciones
import archivos

def registrar_producto(inventario: list) -> None:
    """Registra un nuevo producto en el inventario.
    Args:
        inventario (list): La lista de productos.
    """
    print("\n--- REGISTRAR NUEVO PRODUCTO ---")
    codigo = validaciones.pedir_cadena_no_vacia("Ingrese código único: ")
    es_valido = validaciones.validar_codigo_unico(codigo, inventario)

    while es_valido == False:
        print("Error: El código ya existe.")
        codigo = validaciones.pedir_cadena_no_vacia("Ingrese otro código único: ")
        es_valido = validaciones.validar_codigo_unico(codigo, inventario)
        
    nombre = validaciones.pedir_cadena_no_vacia("Ingrese nombre: ")
    categoria = validaciones.pedir_cadena_no_vacia("Ingrese categoría: ")
    precio = validaciones.pedir_numero_positivo("Ingrese precio: ")
    stock = int(validaciones.pedir_numero_positivo("Ingrese stock disponible: ", True))
    stock_minimo = int(validaciones.pedir_numero_positivo("Ingrese stock mínimo: ", True))
    proveedor = validaciones.pedir_cadena_no_vacia("Ingrese nombre del proveedor: ")
    
    nuevo_producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock,
        "stock_minimo": stock_minimo,
        "proveedor": proveedor
    }
    
    inventario.append(nuevo_producto)
    archivos.guardar_datos(inventario)
    print("¡Producto registrado con éxito!")

def obtener_estado_stock(stock: int, stock_minimo: int) -> str:
    """Determina el estado del stock de un producto.
    Args:
        stock (int): La cantidad de unidades en stock.
        stock_minimo (int): La cantidad mínima de unidades en stock.
    Returns:
        str: El estado del stock (Sin Stock, Stock Bajo o Stock Normal).
    """
    if stock == 0:
        return "Sin Stock"
    elif stock <= stock_minimo:
        return "Stock Bajo"
    else:
        return "Stock Normal"

def mostrar_producto(producto: dict) -> None:
    """Muestra la información de un producto.
    Args:
        producto (dict): El diccionario que contiene la información del producto.
    """
    estado = obtener_estado_stock(producto["stock"], producto["stock_minimo"])
    print(f"Código: {producto['codigo']}")
    print(f"Nombre: {producto['nombre']}")
    print(f"Categoría: {producto['categoria']}")
    print(f"Precio: ${producto['precio']}")
    print(f"Stock: {producto['stock']}")
    print(f"Stock mínimo: {producto['stock_minimo']}")
    print(f"Proveedor: {producto['proveedor']}")
    print(f"Estado: {estado}")
    print("=" * 30)

def listar_productos(inventario: list) -> None:
    """Muestra la lista de todos los productos en el inventario.
    Args:
        inventario (list): La lista de productos.
    """
    print("\n--- LISTADO DE PRODUCTOS  ---")
    if len(inventario) == 0:
        print("No hay productos registrados.")
        return
    # Recorrido con range(len(...))
    for i in range(len(inventario)):
        mostrar_producto(inventario[i])

def buscar_producto_por_codigo(inventario: list) -> None:
    """Busca un producto por su código y muestra su información.
    Args:
        inventario (list): La lista de productos.
    """
    print("\n--- BUSCAR PRODUCTO POR CÓDIGO ---")
    codigo = input("Ingrese el código a buscar: ")
    
    encontrado = False
    for i in range(len(inventario)):
        producto = inventario[i]

        if producto["codigo"] == codigo:
            mostrar_producto(producto)
            encontrado = True
            break
            
    if encontrado == False:
        print("Producto no encontrado.")

def buscar_productos_por_categoria(inventario: list) -> None:
    """Busca productos por su categoría y muestra su información.
    Args:
        inventario (list): La lista de productos.
    """
    print("\n--- BUSCAR POR CATEGORÍA ---")
    categoria = input("Ingrese la categoría: ")
    
    encontrado = False
    for i in range(len(inventario)):
        producto = inventario[i]

        if producto["categoria"] == categoria:
            mostrar_producto(producto)
            encontrado = True
            
    if encontrado == False:
        print("No existen productos registrados para dicha categoría.")

def modificar_producto(inventario: list) -> None:
    """Modifica la información de un producto existente en el inventario.
    Args:
        inventario (list): La lista de productos.
    """
    print("\n--- MODIFICAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto a modificar: ")
    
    indice_encontrado = -1
    for i in range(len(inventario)):
        if inventario[i]["codigo"] == codigo:
            indice_encontrado = i
            break
            
    if indice_encontrado == -1:
        print("Producto no encontrado.")
        return
        
    produ_a_modificar = inventario[indice_encontrado]
    print("Deje en blanco si no desea modificar el campo.")
    
    nombre = input(f"Nombre actual ({produ_a_modificar['nombre']}): ")
    if nombre != "":
        produ_a_modificar["nombre"] = nombre
        
    categoria = input(f"Categoría actual ({produ_a_modificar['categoria']}): ")
    if categoria != "":
        produ_a_modificar["categoria"] = categoria
        
    precio_nuevo = input(f"Precio actual ({produ_a_modificar['precio']}): ")
    if precio_nuevo != "":
        while float(precio_nuevo) <= 0:
            print("El precio debe ser mayor a cero.")
            precio_nuevo = input("Ingrese precio válido: ")
        produ_a_modificar["precio"] = float(precio_nuevo)
        
    stock_nuevo = input(f"Stock actual ({produ_a_modificar['stock']}): ")
    if stock_nuevo != "":
        while int(stock_nuevo) < 0:
            print("El stock no puede ser negativo.")
            stock_in = input("Ingrese stock válido: ")
        produ_a_modificar["stock"] = int(stock_in)
        
    stock_min_nuevo = input(f"Stock mínimo actual ({produ_a_modificar['stock_minimo']}): ")
    if stock_min_nuevo != "":
        while int(stock_min_nuevo) < 0:
            print("El stock mínimo no puede ser negativo.")
            stock_min_nuevo = input("Ingrese stock mínimo válido: ")
        produ_a_modificar["stock_minimo"] = int(stock_min_nuevo)
        
    proveedor = input(f"Proveedor actual ({produ_a_modificar['proveedor']}): ")
    if proveedor != "":
        produ_a_modificar["proveedor"] = proveedor
        
    archivos.guardar_datos(inventario)
    print("¡Producto modificado y guardado con éxito!")

def eliminar_producto(inventario: list) -> None:
    """Elimina un producto del inventario.
    Args:
        inventario (list): La lista de productos.
    """
    print("\n--- ELIMINAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto a eliminar: ")
    
    indice_encontrado = -1
    for i in range(len(inventario)):
        if inventario[i]["codigo"] == codigo:
            indice_encontrado = i
            break
            
    if indice_encontrado == -1:
        print("Producto no encontrado.")
        return
        
    confirmacion = input("¿Está seguro que desea eliminar este producto? (S/N): ")
    if confirmacion == "S" or confirmacion == "s":
        inventario.pop(indice_encontrado)
        archivos.guardar_datos(inventario)
        print("Producto eliminado correctamente.")
    else:
        print("Operación cancelada.")