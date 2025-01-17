import flet as ft

#from routers.enrutamiento import route_change
from Components.barra_de_navegacion import barra_de_navegacion
from routers.enrutamiento import route_change
from routers.routers import Router


def main(page: ft.Page):
    # Configuración inicial de la página
    page.title = "Aplicación Modular"
    page.scroll = "auto"

    # Configuración del NavigationDrawer (barra de navegación)
    barra: ft.NavigationDrawer = barra_de_navegacion(page)
    page.drawer = barra
    page.drawer.open = True  # Cerrado por defecto

    # Ruta inicial
    page.on_route_change = route_change
    page.go(Router.INICIO.value)


ft.app(target=main)
