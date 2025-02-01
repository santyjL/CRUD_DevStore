import flet as ft

from backend.crear_productos import Creador_de_productos
from backend.productos import productos_buscador
from Components.grid import crear_grid
from styles import Colores, Estilos


def buscar_producto(busqueda: str = "") -> list[Creador_de_productos]:
    """
    Función que busca un producto en la lista de productos_totales.
    """
    productos_totales: list[Creador_de_productos] = productos_buscador()

    productos_encontrados: list[Creador_de_productos] = []
    if busqueda == "":
        return productos_totales

    for producto in productos_totales:
        if busqueda.lower() in producto.nombre.lower() or busqueda.lower() in producto.descripcion.lower():
            productos_encontrados.append(producto)

    return productos_encontrados

def buscar_input(page: ft.Page, resultados: ft.Column):
    """
    Función que crea una barra de búsqueda y actualiza los resultados en la página.
    """
    def buscar(e):
        productos = buscar_producto(buscador.value)
        resultados.controls.clear()
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
        page.update()

    buscador = ft.TextField(
        value="",
        label="Buscar",
        width="full",
        cursor_color=Colores.AZUL.value,
        color=Colores.NEGRO.value,
        expand=1
    )
    boton = ft.Button(
        text="Buscar",
        on_click=buscar
    )

    barra_busqueda = ft.Row(
        controls=[
            buscador,
            boton
        ],
        alignment=ft.CrossAxisAlignment.CENTER,
    )

    return barra_busqueda