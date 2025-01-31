import flet as ft

from backend.productos import todos_los_productos
from Components.barra_comprimida import barra_comprimida
from Components.grid import crear_grid
from styles import Colores, Estilos


def buscador_view(page: ft.Page):
    page.title = "Buscador"
    page.bgcolor = Colores.BLANCO.value
    page.scroll = "auto"

    productos =ft.Column(
        controls=[
            ft.Container(
                ft.Row(
                    controls=[
                        crear_grid(todos_los_productos, max_extent=350)
                    ],
                    alignment=ft.CrossAxisAlignment.CENTER,
                ),
                margin= Estilos.Margin.value,
                bgcolor=Colores.GRIS.value,
            )
        ],
    )

    # Contenido de la vista
    page.controls.append(barra_comprimida(page.drawer))
    page.controls.append(productos)