import flet as ft

from backend.crear_productos import Creador_de_productos
from Components.contenedor_productos import contenedor_de_productos
from styles import Estilos


def crear_grid(contenedores : list[Creador_de_productos]) -> ft.GridView:
    """
    Crear un GridView dinámico que muestra una cantidad específica de elementos.

    :param cantidad_elementos: Número de componentes a agregar al GridView.
    :return: Un GridView configurado con los elementos especificados.
    """

    productos = []


    for contenedor in contenedores:  # Crear tantos elementos como se especifique
        nombre, imagen, descripcion, color, width, height, expand = contenedor.elementos_retorno()
        elemento = contenedor_de_productos(
                nombre,               # Nombre dinámico del producto
                imagen,  # Imagen de ejemplo
                descripcion,        # Descripción estática del producto
                color,                # Color de fondo
                width,                      # Ancho del producto
                height,
                expand                  # Altura del producto
            )

        productos.append(elemento)

    # Configurar el GridView
    return ft.GridView(
        expand=True,                 # Hacer que el GridView ocupe el espacio disponible
        max_extent=300,            # Tamaño máximo de cada celda (en píxeles)
        child_aspect_ratio=1.0,      # Relación ancho/alto de cada elemento
        spacing=Estilos.Margin.value,      # Espacio entre columnas
        run_spacing=Estilos.Margin.value,  # Espacio entre filas
        controls=[
            elemento for elemento in productos
        ],
    )
