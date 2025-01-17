import flet as ft

from backend.productos import (producto_nuevo, productos_destacado,
                               productos_varios)
from Components.barra_comprimida import barra_comprimida
from Components.contenedor_productos import contenedor_de_productos
from Components.grid import crear_grid
from styles import Colores, Estilos

(nombre,imagen,descripcion,color,
width,height,expand,color_texto) = producto_nuevo.elementos_retorno()

# Función principal
def inicio_view(page: ft.Page):
    # Configuración de la página
    page.title = "Inicio"
    page.bgcolor = Colores.BLANCO.value
    page.scroll = "auto"

    # Sección "Lo más nuevo"
    lo_mas_nuevo = ft.Column(
        controls=[
            contenedor_de_productos(nombre,imagen,descripcion,color,
                            width,height,expand,color_texto)
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

