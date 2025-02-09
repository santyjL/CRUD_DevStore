import flet as ft

from backend.productos import productos_totales
from Components.barra_comprimida import barra_comprimida
from styles import Colores


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
                                ft.Image(src=imagen, width=600,expand=1)
                            ],

                        ),
                        ft.Column(
                            controls=[
                                ft.Text(nombre, size=30, weight=ft.FontWeight.BOLD, color=Colores.NEGRO.value),
                                ft.Text(descripcion, size=24, color=Colores.GRIS.value),
                                ft.Text(f"Marca: {marca}", size=20, color=Colores.ROJO.value , width=400),
                                ft.Text(f"Categoría: {categoria}", size=20, color=Colores.ROJO.value),
                                ft.Text(f"Precio: {precio}", size=20, color=Colores.ROJO.value),
                            ],
                            width= 400
                        ),
                    ],
                    spacing=50
                )
            )

    page.update()
