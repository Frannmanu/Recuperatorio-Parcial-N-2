import archivos
import productos
import estadisticas

def mostrar_menu():
    inventario = archivos.cargar_datos()
    
    continuar = True
    while continuar == True:
        print("\n=======================================")
        print("  SISTEMA DE GESTIÓN DE INVENTARIO     ")
        print("=======================================")
        print("1. Registrar producto")
        print("2. Listar productos ")
        print("3. Buscar producto por código ")
        print("4. Buscar producto por categoría")
        print("5. Modificar producto")
        print("6. Eliminar producto")
        print("7. Ver Estadísticas")
        print("8. Salir")
        print("=======================================\n")
        
        opcion = input("Seleccione una opción: ")
        
        match opcion:
            case "1":
                productos.registrar_producto(inventario)
            case "2":
                productos.listar_productos(inventario)
            case "3":
                productos.buscar_producto_por_codigo(inventario)
            case "4":
                productos.buscar_productos_por_categoria(inventario)
            case "5":
                productos.modificar_producto(inventario)
            case "6":
                productos.eliminar_producto(inventario)
            case "7":
                estadisticas.mostrar_estadisticas(inventario)
            case "8":
                continuar = False
                print("\nGracias por usar el sistema de gestión de inventario. ¡Hasta luego!")
            case _:
                print("Opcion invalida. Por favor, seleccione una opcion valida.")