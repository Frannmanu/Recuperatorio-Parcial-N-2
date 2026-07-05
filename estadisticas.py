def total_productos(inventario):
    return len(inventario)

def valor_total_inventario(inventario):
    total = 0.0
    for i in range(len(inventario)):
        total += inventario[i]["precio"] * inventario[i]["stock"]
    return total

def precio_promedio(inventario):
    if len(inventario) == 0:
        return 0.0
    total_precios = 0.0
    for i in range(len(inventario)):
        total_precios += inventario[i]["precio"]
    return total_precios / len(inventario)

def producto_mas_caro(inventario):
    if len(inventario) == 0:
        return None
    mas_caro = inventario[0]
    for i in range(len(inventario)):
        if inventario[i]["precio"] > mas_caro["precio"]:
            mas_caro = inventario[i]
    return mas_caro

def producto_mayor_stock(inventario):
    if len(inventario) == 0:
        return None
    mayor_stock = inventario[0]
    for i in range(len(inventario)):
        if inventario[i]["stock"] > mayor_stock["stock"]:
            mayor_stock = inventario[i]
    return mayor_stock

def cantidad_sin_stock(inventario):
    contador = 0
    for i in range(len(inventario)):
        if inventario[i]["stock"] == 0:
            contador += 1
    return contador

def cantidad_stock_bajo(inventario):
    contador = 0
    for i in range(len(inventario)):
        p = inventario[i]
        if p["stock"] != 0 and p["stock"] <= p["stock_minimo"]:
            contador += 1
    return contador

def mostrar_productos_por_categoria(inventario):
    categorias_vistas = []
    
    for i in range(len(inventario)):
        cat = inventario[i]["categoria"]
        
        ya_existe = False
        for j in range(len(categorias_vistas)):
            if categorias_vistas[j] == cat:
                ya_existe = True
                break
                
        if ya_existe == False:
            categorias_vistas.append(cat)
            
    for i in range(len(categorias_vistas)):
        cat_actual = categorias_vistas[i]
        contador = 0
        for j in range(len(inventario)):
            if inventario[j]["categoria"] == cat_actual:
                contador += 1
        print(f" - {cat_actual}: {contador}")

def porcentaje_stock_bajo(inventario):
    total = len(inventario)
    if total == 0:
        return 0.0
    bajo = cantidad_stock_bajo(inventario)
    return (bajo / total) * 100

def mostrar_estadisticas(inventario):
    print("\n--- INFORME ESTADÍSTICO ---")
    if len(inventario) == 0:
        print("No hay datos suficientes para generar estadísticas.")
        return
        
    print(f"Cantidad total de productos: {total_productos(inventario)}")
    print(f"Valor total del inventario: ${valor_total_inventario(inventario)}")
    print(f"Precio promedio de los productos: ${precio_promedio(inventario):.2f}")
    
    caro = producto_mas_caro(inventario)
    print(f"Producto más caro: {caro['nombre']} (${caro['precio']})")
    
    m_stock = producto_mayor_stock(inventario)
    print(f"Producto con mayor stock: {m_stock['nombre']} ({m_stock['stock']} unidades)")
    
    print(f"Cantidad de productos sin stock: {cantidad_sin_stock(inventario)}")
    print(f"Cantidad de productos con stock bajo: {cantidad_stock_bajo(inventario)}")
    
    print("Cantidad de productos por categoría:")
    mostrar_productos_por_categoria(inventario)
    
    print(f"Porcentaje de productos con stock bajo: {porcentaje_stock_bajo(inventario):.2f}%")