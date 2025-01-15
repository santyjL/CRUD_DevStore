import flet as ft

from styles import Colores, Estilos


def imagenes(src, width=None, height=None):
    return ft.Container(
        image_src=src,
        width=width,
        height=height,
        border_radius=Estilos.BORDER_RADIUS_2.value,
        border=ft.border.all(1, Colores.NEGRO.value),  # Ajusta el grosor y color del borde
        bgcolor=Colores.BLANCO.value,  # Fondo del contenedor
        image_fit=ft.ImageFit.COVER,  # Ajuste de la imagen (puede ser CONTAIN o COVER según lo que necesites)
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=6,
            color=ft.colors.BLACK45,
            offset=ft.Offset(2, 2)
        ),  # Sombra alrededor del contenedor
    )
