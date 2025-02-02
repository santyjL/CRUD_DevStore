import flet as ft

from backend.crear_productos import Creador_de_productos
from backend.productos import productos_buscador
from Components.grid import crear_grid
from styles import Colores, Estilos


def sin_informacion(productos_encontrados: list[Creador_de_productos]):

        if productos_encontrados == []:
            return ft.Container(
                ft.Text("No hay productos que coincidan con la búsqueda.",
                        color=Colores.NEGRO.value,
                        size=22),
                alignment=ft.alignment.center,
                margin=Estilos.Margin.value,
            )

        return None

def buscar_producto(busqueda: str = "", categoria: str = None) -> list[Creador_de_productos]:
    """
    Función que busca un producto en la lista de productos_totales.
    """
    productos_totales: list[Creador_de_productos] = productos_buscador()

    productos_encontrados: list[Creador_de_productos] = []
    if categoria == "Todo":
        categoria = None

    if busqueda == "" and categoria is None:
        return productos_totales

    for producto in productos_totales:
        if (busqueda.lower() in producto.nombre.lower() or
            busqueda.lower() in producto.descripcion.lower()) and (categoria is None or
                                                                   producto.categoria == categoria):
            productos_encontrados.append(producto)

    return productos_encontrados

def buscar_input(page: ft.Page, resultados: ft.Column):
    """
    Función que crea una barra de búsqueda y actualiza los resultados en la página.
    """
    def buscar(e):
        productos = buscar_producto(buscador.value, page.client_storage.get("categoria_seleccionada"))
        resultados.controls.clear()

        if productos:
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
        else:
            resultados.controls.append(sin_informacion(productos))

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