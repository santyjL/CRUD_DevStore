import flet as ft

from backend.crear_productos import Creador_de_productos
from backend.productos import productos_buscador


def buscar_producto(busqueda:str = "")->list[Creador_de_productos]:
    """
    Función que busca un producto en la lista de productos_totales.
    """
    productos_totales:list[Creador_de_productos] = productos_buscador()

    productos_encontrados:list[Creador_de_productos] = []
    if busqueda == "":
        return productos_totales

    for producto in productos_totales:
        if busqueda.lower() in producto.nombre.lower():
            productos_encontrados.append(producto)

    return productos_encontrados

