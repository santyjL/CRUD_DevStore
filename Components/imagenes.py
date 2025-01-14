import flet as ft

from styles import Colores, Estilos


def imagenes(src, width=None, height=None):
    return ft.Container(
        image_src=src,
        width=width,
        height=height,
        border_radius=Estilos.BORDER_RADIUS_2.value,
        border=ft.border.all(width , Colores.NEGRO.value),
        )