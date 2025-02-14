import flet as ft

from Components.barra_comprimida import barra_comprimida
from styles import Colores


def vender_view(page: ft.Page):
    page.title = "Buscador"
    page.bgcolor = Colores.BLANCO.value
    page.scroll = "auto"

    page.controls.append(barra_comprimida(page.drawer))
    page.update()
