import flet as ft

from backend.carrito import productos_carrito, productos_del_carrito
from Components.barra_comprimida import barra_comprimida
from Components.grid import crear_grid
from styles import Colores, Estilos


def carrito_view(page: ft.Page):
    page.title = "Carrito"
    page.bgcolor = Colores.BLANCO.value
    page.scroll = "auto"
    # Añadir la barra de navegación comprimida
    page.controls.append(barra_comprimida(page.drawer))
    columna_productos = ft.Column()

    productos_carro = productos_del_carrito()
    columna_productos.controls.append(
        ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        crear_grid(productos_carro, max_extent=450, page=page, contenedor_view=2)
                    ],
                ),
            ],
        )
    )
    page.controls.append(columna_productos)
    page.update()