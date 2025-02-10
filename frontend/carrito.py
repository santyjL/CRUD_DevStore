import flet as ft

from backend.productos import productos_totales
from Components.barra_comprimida import barra_comprimida
from styles import Colores


def carrito_view(page: ft.Page):
    page.title = "Carrito"
    page.bgcolor = Colores.BLANCO.value
    page.scroll = "auto"
    # Añadir la barra de navegación comprimida
    page.controls.append(barra_comprimida(page.drawer))

    page.update()