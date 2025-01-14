import flet as ft

from backend.productos import productos_destacado, productos_varios
from Components.barra_de_navegacion import (barra_comprimida,
                                            barra_de_navegacion)
from Components.contenedor_productos import contenedor_de_productos
from Components.grid import crear_grid
from styles import Colores, Estilos


# Función principal
def main(page: ft.Page):
    # Configuración de la página
    page.title = "Inicio"
    page.bgcolor = Colores.BLANCO.value
    page.scroll = "auto"

    # Barra de navegación
    barra: ft.NavigationDrawer = barra_de_navegacion(page)
    page.drawer = barra  # `barra` es el AnimatedSwitcher que contiene el NavigationDrawer
    page.drawer.open = False  # La barra de navegación estará cerrada por defecto

    # Sección "Lo más nuevo"
    lo_mas_nuevo = ft.Column(
        controls=[
            contenedor_de_productos(
                "Nuevo Producto",
                "https://via.placeholder.com/150",
                "Descripción del producto",
                Colores.ROJO.value,
                width="full", height=400,
                expand= 1
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    lo_mas_destacado =ft.Container(
        ft.Row(
            controls=[
                crear_grid(productos_destacado, max_extent=450)

            ],
            alignment=ft.CrossAxisAlignment.CENTER,
        ),

    )

    otros =ft.Column(
        controls=[
            ft.Container(
                ft.Row(
                    controls=[
                        crear_grid(productos_varios, max_extent=300)
                    ],
                    alignment=ft.CrossAxisAlignment.CENTER,
                ),
                margin= Estilos.Margin.value,
                bgcolor=Colores.GRIS.value,
            )
        ],
    )

    # Añadir la sección "Lo más nuevo" a la página
    page.controls.append(barra_comprimida(page.drawer))
    page.controls.append(lo_mas_nuevo)
    page.controls.append(lo_mas_destacado)
    page.controls.append(otros)
    page.update()

ft.app(target=main)