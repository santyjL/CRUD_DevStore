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
                        crear_grid(productos_carro, max_extent=450, page=page)
                    ],
                ),
            ],
        )
    )

    if productos_carro:
        barra_acciones = ft.Row(
            controls=[
                ft.Button(text="Comprar", on_click=lambda e: comprar_productos_carrito(page)),
                ft.Button(text="Eliminar", on_click=lambda e: eliminar_producto_carrito(page))
            ],
            alignment=ft.MainAxisAlignment.END,
            spacing=10,
        )
        page.controls.append(barra_acciones)

    else:
        barra_acciones = ft.Row(
            controls=[
                ft.Text(value="No hay nada en el carrito de compreas",size=28),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        )
        page.controls.append(barra_acciones)

    page.controls.append(columna_productos)
    page.update()

def eliminar_producto_carrito(page: ft.Page):
    # Lógica para eliminar productos del carrito
    productos_carrito.clear()
    page.controls.clear()
    carrito_view(page)

def comprar_productos_carrito(page: ft.Page):
    # Lógica para comprar productos del carrito
    # Aquí puedes añadir la lógica para procesar la compra
    productos_carrito.clear()
    page.controls.clear()
    carrito_view(page)