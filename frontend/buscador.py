import flet as ft

from Components.barra_comprimida import barra_comprimida
from styles import Colores


def buscador_view(page: ft.Page):
    page.title = "Buscador"
    page.bgcolor = Colores.BLANCO.value
    page.scroll = "auto"

    # Contenido de la vista
    page.controls.append(barra_comprimida(page.drawer))
    page.controls.append(ft.Text("Página del Buscador"))