import flet as ft

from Components.imagenes import imagenes
from routers.routers import Router
from styles import Colores, Estilos


def contenedor_de_productos(titulo, imagen_src, descripcion,
                            bgcolor, width="auto", height=400,
                            expand = False, color_texto =Colores.BLANCO.value,categoria=None,
                            page=ft.Page):
    def abrir_producto(e):
        page.go(route=Router.PRODUCTO.value)

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(titulo, size=20, weight=ft.FontWeight.BOLD, color=color_texto),
                imagenes(src=imagen_src, width="full", height=height),
                ft.Text(descripcion, size=14, color=color_texto),
                ft.Text(categoria, size=18,italic=True,
                        color=color_texto, bgcolor=Colores.GRIS.value, )
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
        on_click=abrir_producto
    )