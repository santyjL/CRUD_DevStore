import flet as ft

from backend.productos import productos_totales
from Components.barra_comprimida import barra_comprimida
from styles import Colores, Estilos


def productos_view(page: ft.Page):
    page.title = "Producto"
    page.bgcolor = Colores.BLANCO.value
    page.scroll = "auto"
    id = int(page.route.split(" ")[1])

    # Añadir la barra de navegación comprimida
    page.controls.append(barra_comprimida(page.drawer))

    # Añadir contenido simple en blanco
    for i in range(len(productos_totales)):

        if productos_totales[i].id == id:
            (nombre,imagen,descripcion,
            color,width,height,expand,color_texto,
            categoria,marca,precio,id) = productos_totales[i].elementos_retorno()

            page.controls.append(
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Image(src=imagen, width="full", height=500,expand=1)
                            ]
                        ),
                        ft.Column(
                            controls=[
                                ft.Text(nombre, size=20, weight=ft.FontWeight.BOLD, color=color_texto),
                                ft.Text(descripcion, size=14, color=color_texto),
                                ft.Text(f"Marca: {marca}", size=14, color=color_texto),
                                ft.Text(f"Categoría: {categoria}", size=14, color=color_texto),
                                ft.Text(f"Precio: {precio}", size=14, color=color_texto),
                            ]
                        )
                    ]
                )
            )

    page.update()
