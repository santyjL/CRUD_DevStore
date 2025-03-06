import flet as ft

from backend.crear_productos import Creador_de_productos
from Components.barra_comprimida import barra_comprimida
from Components.crear_productos_nuevos import abrir_modal_agregar_producto
from styles import Colores


def vender_view(page: ft.Page):
    page.title = "Buscador"
    page.bgcolor = Colores.BLANCO.value
    page.scroll = "auto"

    # Botón para abrir el modal de agregar producto
    btn_agregar = ft.ElevatedButton(
        "Agregar Producto",
        on_click=lambda e: abrir_modal_agregar_producto(page),
        width=200,
        height=50,
        bgcolor=Colores.ROJO.value,
    )

    page.controls.append(barra_comprimida(page.drawer))
    # Mostrar el botón en la pantalla de vender
    page.controls.append(
        ft.Column(
            controls=[
                btn_agregar,
                ft.Container(
                    content=ft.Text("Si tiene algún producto que quiera vender puede añadirlo solamente completando el formulario",
                                    size=18),
                    alignment=ft.alignment.center,
                    padding=20
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
    page.update()
