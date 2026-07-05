# Sistema de Gestión de Inventario (electrónicos)

Este proyecto es una aplicación de consola desarrollada en **Python** diseñada para administrar de forma eficiente el inventario de una empresa de artículos electrónicos. Permite registrar, listar, buscar, modificar y eliminar productos, además de generar informes estadísticos detallados.

Toda la información se almacena de forma permanente en un archivo en formato **JSON**, asegurando que los datos no se pierdan entre diferentes ejecuciones del programa.

---

## 🛠️ Características Principales

* **Estructura Modular:** El código está dividido en módulos independientes con responsabilidades claras (`main.py`, `menu.py`, `productos.py`, `archivos.py`, `estadisticas.py`, `validaciones.py`, `productos.json`).
* **Persistencia de Datos:** Uso de la librería nativa `json` para leer y escribir el inventario en el archivo `productos.json` de forma automática tras cada cambio.
* **Validaciones Robustas:** Control de datos de entrada (códigos únicos, precios mayores a cero, control de stock negativo y campos obligatorios).
* **Lógica Pura de Programación:** Implementado utilizando estructuras de control fundamentales para mantener el código legible y accesible.

---

## 📂 Estructura del Proyecto

El sistema se compone de los siguientes archivos:

* **`main.py`:** Punto de entrada obligatorio del sistema. Inicializa el programa llamando al menú principal.
* **`menu.py`:** Contiene el bucle principal de la interfaz de consola y deriva las acciones según la opción elegida por el usuario.
* **`productos.py`:** Maneja la lógica central del ABM (Alta, Baja, Modificación) y las búsquedas por código o categoría.
* **`archivos.py`:** Gestiona la lectura y escritura segura del archivo.
* **`estadisticas.py`:** Funciones independientes para calcular totales, promedios, valores acumulados de inventario y estados de stock.
* **`validaciones.py`:** Concentra las reglas de negocio para asegurar que los datos ingresados sean correctos.

---

## 🚀 Cómo Ejecutar el Proyecto

1. **Clonar el repositorio** (o descargar los archivos en una misma carpeta):
   ```bash
   git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/Frannmanu/Recuperatorio-Parcial-N-2.git)
---

## 📖 Guía de Uso Rápido (Paso a Paso)

Para probar el sistema de forma correcta y ver cómo interactúan los módulos, te sugerimos seguir estos pasos:
![alt text](image.png)
1. **Registrar un Producto (Opción 1):** * Al iniciar, el inventario estará vacío. Seleccioná la opción `1` para agregar tu primer artículo.
   * Ingresá un código (por ejemplo: `P001`), un nombre (`Notebook Lenovo`), una categoría (`Informática`), un precio (`1250000`), un stock (`8`) y un stock mínimo (`5`).

2. **Listar el Inventario (Opción 2):**
   * Seleccioná la opción `2` para ver todos los productos guardados. 
   * Vas a notar que el sistema calcula automáticamente el campo **Estado**. En el ejemplo anterior, como el stock (8) es mayor al mínimo (5), verás `Estado: Stock Normal`.

3. **Verificar la Persistencia (JSON):**
   * Salí del programa con la opción `8`.
   * Abrí el archivo `productos.json` en tu editor. Vas a ver que la librería guardó el producto con formato de texto estructurado de forma automática.
   * Volvé a iniciar el programa con `python main.py` y usá la opción `2`; verás que el producto sigue ahí.

4. **Monitorear Alertas de Stock:**
   * Registrá otro producto (ej: `P002`, `Mouse Logitech`) con un stock de `2` y un stock mínimo de `5`.
   * Al listarlo o ir a la sección de **Estadísticas (Opción 7)**, el sistema te alertará que tenés `1` producto con **Stock Bajo**, calculando también los porcentajes de reposición de la empresa.

5. **Modificar o Eliminar (Opciones 5 y 6):**
   * Si querés actualizar el stock de un producto, elegí la opción `5`, ingresá su código y modificá solo el campo numérico del stock. 
   * Si deseás borrarlo, la opción `6` te pedirá confirmación (`S/N`) antes de eliminarlo definitivamente del archivo, en caso de seleccionar la opcion por error.

--

## 👨‍🎓 Participante:
    Franco Dominguez.