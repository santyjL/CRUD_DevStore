import flet as ft

from backend.productos import categorias, productos_buscador
from Components.barra_comprimida import barra_comprimida
from Components.buscar import buscar_input, buscar_producto
from Components.grid import crear_grid
from styles import Colores, Estilos


def productos_view(page: ft.Page):
    page.title = "Producto"
    page.bgcolor = Colores.BLANCO.value
    page.scroll = "auto"

    # Añadir la barra de navegación comprimida
    page.controls.append(barra_comprimida(page.drawer))

    # Añadir contenido simple en blanco
    page.controls.append(
        ft.Container(
            content=ft.Text("Detalles del Producto", size=30, weight=ft.FontWeight.BOLD),
            alignment=ft.alignment.center,
            bgcolor=Colores.BLANCO.value,
            expand=True
        )
    )

    page.update()
