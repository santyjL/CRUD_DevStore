import flet as ft

from backend.crear_productos import Creador_de_productos
from Components.contenedor_productos import contenedor_de_productos
from styles import Estilos


def crear_grid(contenedores: list[Creador_de_productos], max_extent, page) -> ft.GridView:
    """
    Crear un GridView dinámico que muestra una cantidad específica de elementos.
    :param contenedores: Lista de contenedores de productos
    :param max_extent: Tamaño máximo de cada celda (en píxeles)
    :param page: Página actual de Flet
    :return: GridView con los productos
    """

    productos = []

    for contenedor in contenedores:  # Crear tantos elementos como se especifique
        (nombre, imagen, descripcion,
         color, width, height, expand,
         color_texto, categoria, marca, precio, id) = contenedor.elementos_retorno()

        elemento = contenedor_de_productos(
            titulo=nombre,                 # Nombre dinámico del producto
            imagen_src=imagen,             # Imagen de ejemplo
            descripcion=descripcion,       # Descripción estática del producto
            bgcolor=color,                 # Color de fondo
            width=width,                   # Ancho del producto
            height=height,                 # Altura del producto
            expand=expand,                 # Expandir el producto
            color_texto=color_texto,       # Color del texto
            categoria=categoria,           # Categoría del producto
            page=page,                     # Página actual
            id=id                          # ID del producto
        )

        productos.append(elemento)

    # Configurar el GridView
    return ft.GridView(
        expand=True,                 # Hacer que el GridView ocupe el espacio disponible
        max_extent=max_extent,       # Tamaño máximo de cada celda (en píxeles)
        child_aspect_ratio=1.0,      # Relación ancho/alto de cada elemento
        spacing=Estilos.Margin.value,      # Espacio entre columnas
        run_spacing=Estilos.Margin.value,  # Espacio entre filas
        controls=productos,          # Añadir los productos al GridView
    )

