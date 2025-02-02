import flet as ft

from backend.productos import categorias, productos_buscador
from Components.barra_comprimida import barra_comprimida
from Components.buscar import buscar_input, buscar_producto
from Components.grid import crear_grid
from styles import Colores, Estilos


def buscador_view(page: ft.Page):
    page.title = "Buscador"
    page.bgcolor = Colores.BLANCO.value
    page.scroll = "auto"

    resultados = ft.Column()

    barra_de_busqueda = buscar_input(page, resultados)

    productos = productos_buscador()
    resultados.controls.append(
        ft.Column(
            controls=[
                ft.Container(
                    ft.Row(
                        controls=[
                            crear_grid(productos, max_extent=350)
                        ],
                        alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    margin=Estilos.Margin.value,
                    bgcolor=Colores.GRIS.value,
                ),
            ],
        )
    )

    page.controls.append(barra_comprimida(page.drawer))
    page.controls.append(barra_de_busqueda)
    page.controls.append(resultados)
    page.update()
