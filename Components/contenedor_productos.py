import flet as ft

from styles import Estilos


def contenedor_de_productos(titulo, imagen_src, descripcion,
                            bgcolor, width="auto", height=400,
                            expand = False):
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(titulo, size=20, weight=ft.FontWeight.BOLD),
                ft.Image(src=imagen_src, width=None, height=150),
                ft.Text(descripcion, size=14)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        bgcolor=bgcolor,
        width=width,
        height=height,
        alignment=ft.alignment.center,
        padding=10,
        margin=Estilos.Margin.value,
        expand=expand,
        border_radius=ft.border_radius.all(10),
    )