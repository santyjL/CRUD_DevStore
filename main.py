import flet as ft

from Components.barra_de_navegacion import barra_de_navegación
from styles import Colores


def create_product_container(title, image_src, description, bgcolor):
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(title, size=20, weight=ft.FontWeight.BOLD),
                ft.Image(src=image_src, width=150, height=150),
                ft.Text(description, size=14)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        bgcolor=bgcolor,
        width=None,
        height=200,
        alignment=ft.alignment.center,
        padding=10,
        margin=5,
        border_radius=ft.border_radius.all(10),
    )

def main(page: ft.Page):
    page.title = "Inicio"
    page.bgcolor = Colores.BLANCO.value
    page.scroll = True
    page.adaptive = True

    lo_mas_nuevo = ft.Column(
        controls=[
            create_product_container("Nuevo Producto",
                                     "https://via.placeholder.com/auto",
                                     "Descripción del producto", Colores.ROJO.value)
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        height=800
    )

    Destacado = ft.Row(
        controls=[
            create_product_container("Producto Destacado",
                                     "https://via.placeholder.com/150",
                                     "Descripción del producto", Colores.AZUL.value)
            for _ in range(2)
        ],
        height=400,
        alignment=ft.MainAxisAlignment.CENTER
    )

    productos = ft.Container(
        content=ft.Row(
            controls=[
                create_product_container("Producto",
                                         "https://via.placeholder.com/150",
                                         "Descripción del producto",
                                         Colores.BLANCO.value)
                for _ in range(5)
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        bgcolor=Colores.GRIS.value,
        padding=10,
        border_radius=ft.border_radius.all(10),
        width=None,
        height=400
    )

    barra = barra_de_navegación(page)

    page.add(
        ft.ElevatedButton("Show drawer", on_click=lambda e: page.open(barra)),
        lo_mas_nuevo,
        ft.Container(height=5),
        Destacado,
        ft.Container(height=5),
        productos
    )

if __name__ == "__main__":
    ft.app(target=main)
