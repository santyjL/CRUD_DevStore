import flet as ft

from backend.productos import productos_buscador
from Components.barra_comprimida import barra_comprimida
from Components.buscar import buscar_producto
from Components.grid import crear_grid
from styles import Colores, Estilos

todos_los_productos = productos_buscador()

def buscador_view(page: ft.Page):
    page.title = "Buscador"
    page.bgcolor = Colores.BLANCO.value
    page.scroll = "auto"

    productos =ft.Column(
        controls=[
            ft.Container(
                ft.Row(
                    controls=[
                        crear_grid(buscar_producto(""), max_extent=350)
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